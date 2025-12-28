from .config import load_config
from .database import init_db
from .usage import power_on, power_off, print_start, print_end, get_stats
from .maintenance import check, reset
from .alerts import send_alert
from .exporters import export_json, export_csv


class PrinterMaintenanceManager:
    def __init__(self, config):
        self.server = config.get_server()
        self.printer = config.get_name()

        init_db(self.printer)

        # --- API ENDPOINTS ---
        self.server.register_endpoint(
            "/machine/maintenance/status",
            ["GET"],
            self.handle_status
        )

        self.server.register_endpoint(
            "/machine/maintenance/reset",
            ["POST"],
            self.handle_reset
        )

        self.server.register_endpoint(
            "/machine/maintenance/export",
            ["GET"],
            self.handle_export
        )

        # --- EVENTS ---
        self.server.register_event_handler("klippy:connect", self.on_connect)
        self.server.register_event_handler("klippy:disconnect", self.on_disconnect)
        self.server.register_event_handler("job:start", self.on_print_start)
        self.server.register_event_handler("job:complete", self.on_print_end)
        self.server.register_event_handler("job:error", self.on_print_end)

    # ---------------- EVENTS ----------------

    def on_connect(self):
        power_on(self.printer)

    def on_disconnect(self):
        power_off(self.printer)

    def on_print_start(self, *args):
        print_start(self.printer)

    def on_print_end(self, *args):
        print_end(self.printer)

        due_tasks, hours = check(self.printer)
        for task in due_tasks:
            send_alert(
                f"⚠️ [{self.printer}] Maintenance required: "
                f"{task} ({hours:.1f}h)"
            )

    # ---------------- API ----------------

    async def handle_status(self, request):
        due, hours = check(self.printer)
        stats = get_stats(self.printer)

        return {
            "printer": self.printer,
            "print_hours": stats["print_hours"],
            "power_hours": stats["power_hours"],
            "maintenance_due": due
        }

    async def handle_reset(self, request):
        data = request.get_json()
        reset(self.printer, data["task"], data["hours"])
        return {"status": "ok"}
    async def handle_export(self, request):
        fmt = request.get_argument("format", "json")

        if fmt == "csv":
            return {
                "format": "csv",
                "data": export_csv(self.printer)
            }

        return {
            "format": "json",
            "data": export_json(self.printer)
        }

def load_component(config):
    return PrinterMaintenanceManager(config)

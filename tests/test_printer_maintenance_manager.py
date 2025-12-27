from printer_maintenance_manager.plugin import PrinterMaintenanceManager


class MockServer:
    def register_endpoint(self, *args, **kwargs):
        pass

    def register_event_handler(self, *args, **kwargs):
        pass


class MockConfig:
    def get_server(self):
        return MockServer()

    def get_name(self):
        return "test_printer"


def test_plugin_loads():
    plugin = PrinterMaintenanceManager(MockConfig())
    assert plugin is not None

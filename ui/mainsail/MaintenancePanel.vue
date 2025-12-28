<template>
  <v-card>
    <v-card-title class="d-flex justify-space-between">
      🛠️ Printer Maintenance Manager
      <v-btn icon @click="load">
        <v-icon>mdi-refresh</v-icon>
      </v-btn>
    </v-card-title>

    <v-card-text>
      <v-row>
        <v-col cols="6">
          <strong>🖨️ Print Hours</strong><br />
          {{ data.print_hours }} h
        </v-col>
        <v-col cols="6">
          <strong>⚡ Power Hours</strong><br />
          {{ data.power_hours }} h
        </v-col>
      </v-row>

      <v-divider class="my-3"></v-divider>

      <div v-if="data.maintenance_due.length">
        <v-alert
          v-for="task in data.maintenance_due"
          :key="task"
          type="warning"
          dense
          class="mb-2"
        >
          <div class="d-flex justify-space-between align-center">
            <span>⚠️ {{ task }}</span>
            <v-btn small color="primary" @click="reset(task)">
              Reset
            </v-btn>
          </div>
        </v-alert>
      </div>

      <v-alert v-else type="success" dense>
        ✅ No maintenance required
      </v-alert>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "MaintenancePanel",
  data() {
    return {
      data: {
        print_hours: 0,
        power_hours: 0,
        maintenance_due: []
      }
    }
  },
  mounted() {
    this.load()
  },
  methods: {
    async load() {
      const res = await fetch("/machine/maintenance/status")
      this.data = await res.json()
    },
    async reset(task) {
      await fetch("/machine/maintenance/reset", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          task: task,
          hours: this.data.print_hours
        })
      })
      this.load()
    }
  }
}
</script>

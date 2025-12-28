<template>
  <v-card class="dashboard-widget">
    <v-card-title class="d-flex justify-space-between align-center">
      <span>
        <v-icon left small>mdi-wrench</v-icon>
        Maintenance
      </span>
      <v-btn icon small @click="load">
        <v-icon small>mdi-refresh</v-icon>
      </v-btn>
    </v-card-title>

    <v-card-text>
      <v-row dense>
        <v-col cols="6">
          <div class="caption">Print Hours</div>
          <div class="text-h6">{{ data.print_hours }} h</div>
        </v-col>
        <v-col cols="6">
          <div class="caption">Power Hours</div>
          <div class="text-h6">{{ data.power_hours }} h</div>
        </v-col>
      </v-row>

      <v-divider class="my-2"></v-divider>

      <div v-if="data.maintenance_due.length">
        <v-chip
          v-for="task in data.maintenance_due"
          :key="task"
          color="warning"
          text-color="black"
          small
          class="mb-1 mr-1"
        >
          {{ task }}
          <v-icon
            right
            small
            @click.stop="reset(task)"
          >
            mdi-check
          </v-icon>
        </v-chip>
      </div>

      <v-alert
        v-else
        dense
        type="success"
        text
      >
        No maintenance required
      </v-alert>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "MaintenanceWidget",
  data() {
    return {
      data: {
        print_hours: 0,
        power_hours: 0,
        maintenance_due: []
      }
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    async load() {
      const res = await fetch("/machine/maintenance/status");
      this.data = await res.json();
    },
    async reset(task) {
      await fetch("/machine/maintenance/reset", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          task: task,
          hours: this.data.print_hours
        })
      });
      this.load();
    }
  }
};
</script>

<style scoped>
.dashboard-widget {
  height: 100%;
}
.caption {
  font-size: 12px;
  opacity: 0.7;
}
</style>

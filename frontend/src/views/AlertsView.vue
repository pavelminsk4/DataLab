<template>
  <AlertsScreen :alerts="alerts" @create-alert="createAlerts" />
</template>

<script>
import {createNamespacedHelpers, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import AlertsScreen from '@components/alerts/AlertsScreen'

const {mapActions, mapGetters: mapGettersAlerts} =
  createNamespacedHelpers('alerts')

export default {
  name: 'AlertsView',
  components: {AlertsScreen},
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
    ...mapGettersAlerts({
      alerts: get.ALERTS,
    }),
  },
  async created() {
    if (!this.alerts.length) {
      await this[action.GET_ALERTS](this.department.id)
    }
  },
  methods: {
    ...mapActions([action.GET_ALERTS]),
    createAlerts() {
      this.$router.push({
        name: 'AlertStep1',
      })
    },
  },
}
</script>

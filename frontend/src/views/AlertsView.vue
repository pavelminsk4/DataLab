<template>
  <AlertsScreen :alerts="alerts" @create-alert="createAlerts" />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import AlertsScreen from '@/components/alerts/AlertsScreen'

export default {
  name: 'AlertsView',
  components: {AlertsScreen},
  computed: {
    ...mapGetters({
      alerts: get.ALERTS,
      department: get.DEPARTMENT,
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

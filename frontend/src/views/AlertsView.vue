<template>
  <AlertsScreen @create-alert="createAlerts" />
</template>

<script>
import AlertsScreen from '@/components/alerts/AlertsScreen'

export default {
  name: 'AlertsView',
  components: {AlertsScreen},
  methods: {
    createAlerts() {
      this.$router.push({
        name: 'AlertStep1',
      })
    },
  },
}
</script>

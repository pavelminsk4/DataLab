<template>
  <MainLayout>
    <ReportsScreen v-if="false" />
    <AlertsScreen />
  </MainLayout>
</template>

<script>
import MainLayout from '@/components/layout/MainLayout'
import ReportsScreen from '@/components/project/screens/ReportsScreen'
import AlertsScreen from '@/components/project/screens/AlertsScreen'

export default {
  name: 'ProjectReports',
  components: {AlertsScreen, ReportsScreen, MainLayout},
}
</script>

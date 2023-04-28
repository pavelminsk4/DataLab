<template>
  <MainLayout
    :is-two-columns="currentStep !== 'step3'"
    class="create-alert-wrapper"
  >
    <template #default>
      <div class="create-alert-step-content">
        <MainLayoutTitleBlock
          title="Alerts"
          description="Set up alerts for your project with highly customized filters"
          :back-page="{
            name: 'main page',
            routName: 'MainView',
          }"
        />

        <AlertsProgressBar :step="currentStep" />

        <div class="step-content">
          <router-view></router-view>
        </div>
      </div>
    </template>

    <template #second-column>
      <div class="second-column">
        <router-view name="secondColumn"></router-view>
      </div>
    </template>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'

import MainLayout from '@/components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import AlertsProgressBar from '@/components/alerts/AlertsProgressBar'

const {mapGetters: mapGettersAlerts} = createNamespacedHelpers('alerts')

export default {
  name: 'CreateAlertView',
  components: {MainLayout, MainLayoutTitleBlock, AlertsProgressBar},
  computed: {
    ...mapGettersAlerts([get.CREATE_ALERTS_STEP]),
    currentStep() {
      return `step${this[get.CREATE_ALERTS_STEP]}`
    },
  },
}
</script>

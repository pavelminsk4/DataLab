<template>
  <BaseModal modal-frame-style="width: 90vw; height: 80vh;">
    <div class="main-title">{{ contentVolumeWidget.title }}</div>

    <div class="settings-wrapper">
      <section class="chart-wrapper">
        <div class="chart-title">Content Volume</div>
        <ChartsView
          :is-line="isLineChart"
          :is-bar="isBarChart"
          :chart-labels="volumeLabels"
          :chart-value="volumeValue"
          class="charts"
        />
      </section>

      <div class="general-wrapper-settings">
        <SettingsButtons @update-setting-panel="updateSettingPanel" />

        <BasicSettingsScreen
          v-if="panelName === 'General'"
          :aggregation-periods="aggregationPeriods"
          @save-changes="saveChanges"
          @get-widget-params="updateAggregationPeriod"
        />
      </div>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import ChartsView from '@/components/project/widgets/charts/ChartsView'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'

export default {
  name: 'ContentVolumeSettingsModal',
  components: {
    SettingsButtons,
    BasicSettingsScreen,
    ChartsView,
    BaseModal,
  },
  props: {
    volume: {
      type: [Array, Object],
      required: true,
    },
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      panelName: 'General',
    }
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS}),
    aggregationPeriods() {
      return ['Hour', 'Day', 'Month', 'Year']
    },
    contentVolumeWidget() {
      return this.widgets['volume_widget']
    },
    volumeData() {
      return Object.values(this.volume)
    },
    volumeLabels() {
      return this.volumeData.map((el) => this.formatDate(el.date))
    },
    volumeValue() {
      return this.volumeData.map((el) => el.created_count)
    },
    isLineChart() {
      return this.volumeValue?.length > 7
    },
    isBarChart() {
      return this.volumeValue?.length <= 7
    },
    chartData() {
      return {
        labels: this.volumeLabels,
        legend: {
          display: false,
        },
        datasets: [
          {
            data: this.volumeValue,
            backgroundColor: ['rgba(5, 95, 252, 0.2)'],
            borderColor: ['#055FFC'],
            borderWidth: 1,
            tension: 0.4,
          },
        ],
      }
    },
    chartOptions() {
      return {
        plugins: {
          legend: false,
        },
        responsive: true,
        maintainAspectRatio: false,
      }
    },
  },
  methods: {
    ...mapActions([
      action.GET_VOLUME_WIDGET,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
    ]),
    formatDate(date) {
      return new Date(date).toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    updateAggregationPeriod(val) {
      try {
        this[action.GET_VOLUME_WIDGET]({
          projectId: this.projectId,
          value: val.toLowerCase(),
        })
      } catch (e) {
        console.log(e)
      }
    },
    saveChanges(title, description, agreggationPeriod) {
      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          volume_widget: {
            id: this.contentVolumeWidget.id,
            title: title || this.contentVolumeWidget.title,
            description: description || this.contentVolumeWidget.description,
            aggregation_period:
              agreggationPeriod.toLowerCase() ||
              this.contentVolumeWidget.aggregation_period,
          },
        },
      })
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    updateSettingPanel(val) {
      this.panelName = val
    },
  },
}
</script>

<style lang="scss" scoped>
.main-title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}

.general-wrapper-settings {
  flex: 1;
}

.settings-wrapper {
  display: flex;
  gap: 52px;

  min-width: 100%;

  .chart-wrapper {
    display: flex;
    flex-direction: column;
    flex: 1;

    padding: 18px 50px 34px 26px;

    background: #242529;
    border: 1px solid #2d2d31;
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 10px;

    .chart-title {
      margin-bottom: 25px;

      font-style: normal;
      font-weight: 500;
      font-size: 14px;
      line-height: 110%;
      color: var(--primary-text-color);
    }
  }
}
</style>

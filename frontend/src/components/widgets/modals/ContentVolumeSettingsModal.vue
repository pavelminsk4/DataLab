<template>
  <BaseModal modal-frame-style="width: 90vw; height: 80vh;">
    <div class="main-title">Content Volume</div>

    <div class="settings-wrapper">
      <section class="chart-wrapper">
        <ChartsView
          :chart-data="chartData"
          :chart-options="chartOptions"
          :is-line="isLineChart"
          :is-bar="isBarChart"
        />
      </section>

      <div class="options-wrapper">
        <div class="title-general">General</div>

        <div class="title">Date Aggregation Period</div>
        <BaseSelect
          v-model="aggregationPeriod"
          :list="aggregationPeriods"
          :is-reject-selection="false"
          @select-option="selectItem"
          name="aggregation-period"
          class="option"
        />

        <BaseButton @click="saveOptions">Save</BaseButton>
      </div>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions} from 'vuex'
import {action} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import ChartsView from '@/components/widgets/charts/ChartsView'
import BaseSelect from '@/components/BaseSelect'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'ContentVolumeSettingsModal',
  components: {BaseButton, BaseSelect, ChartsView, BaseModal},
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
      aggregationPeriod: '',
    }
  },
  computed: {
    aggregationPeriods() {
      return ['Hour', 'Day', 'Month', 'Year']
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
    ...mapActions([action.GET_VOLUME_WIDGET]),
    formatDate(date) {
      return new Date(date).toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    selectItem(name, val) {
      try {
        this[action.GET_VOLUME_WIDGET]({
          projectId: this.projectId,
          value: val.toLowerCase(),
        })
      } catch (e) {
        console.log(e)
      }
    },
    saveOptions() {
      this[action.GET_VOLUME_WIDGET]({
        projectId: this.projectId,
        value: this.aggregationPeriod.toLowerCase(),
      })
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

.settings-wrapper {
  display: flex;

  min-width: 100%;

  .chart-wrapper {
    display: flex;
    flex: 1;
  }

  .options-wrapper {
    display: flex;
    flex-direction: column;
    flex: 1;

    margin-right: 30px;

    .title-general {
      padding-bottom: 10px;
      margin-bottom: 40px;

      border-bottom: 1px solid var(--primary-button-color);

      font-weight: 400;
      font-size: 14px;
      line-height: 22px;
    }

    .title {
      margin-bottom: 12px;

      font-style: normal;
      font-weight: 500;
      font-size: 14px;
      line-height: 110%;
    }

    .option {
      margin-bottom: 25px;
    }
  }
}
</style>

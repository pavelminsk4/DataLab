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

      <div class="options-wrapper">
        <div class="title-general">General</div>

        <div class="title">Widget Title</div>
        <BaseInput v-model="title" class="input-title" />

        <div class="title">Widget Description</div>
        <textarea
          class="description-field"
          placeholder="Some words about Widgets"
          v-model="description"
        />

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
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import ChartsView from '@/components/project/widgets/charts/ChartsView'
import BaseSelect from '@/components/BaseSelect'
import BaseButton from '@/components/buttons/BaseButton'
import BaseInput from '@/components/BaseInput'

export default {
  name: 'ContentVolumeSettingsModal',
  components: {BaseInput, BaseButton, BaseSelect, ChartsView, BaseModal},
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
      title: '',
      description: '',
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
    selectItem(name, val) {
      try {
        this.aggregationPeriod = val
        this[action.GET_VOLUME_WIDGET]({
          projectId: this.projectId,
          value: val.toLowerCase(),
        })
      } catch (e) {
        console.log(e)
      }
    },
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          volume_widget: {
            id: this.contentVolumeWidget.id,
            title: this.title || this.contentVolumeWidget.title,
            description:
              this.description || this.contentVolumeWidget.description,
            aggregation_period:
              this.aggregationPeriod.toLowerCase() ||
              this.contentVolumeWidget.aggregation_period,
          },
        },
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
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

.input-title {
  width: 100%;
}

.description-field {
  width: 100%;
  height: 132px;
  padding: 12px 16px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);

  resize: none;
}

.description-field::placeholder {
  color: var(--secondary-text-color);
}

.description-field::-webkit-scrollbar {
  width: 10px;
}

.description-field::-webkit-scrollbar-track {
  border-radius: 10px;

  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

.description-field::-webkit-scrollbar-thumb {
  width: 8px;

  border-radius: 10px;

  background-color: var(--box-shadow-color);
  outline: none;
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

  .options-wrapper {
    display: flex;
    flex-direction: column;
    flex: 1;

    margin-right: 30px;

    .title-general {
      padding-bottom: 10px;
      margin-bottom: 15px;

      border-bottom: 1px solid var(--primary-button-color);

      font-weight: 400;
      font-size: 14px;
      line-height: 22px;
    }

    .title {
      margin: 25px 0 12px;

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

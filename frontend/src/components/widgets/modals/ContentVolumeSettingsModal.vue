<template>
  <BaseModal modal-frame-style="width: 90vw; height: 80vh;">
    <div class="main-title">Content Volume</div>

    <div class="settings-wrapper">
      <section class="chart-wrapper">
        <ChartsView :chart-data="chartData" :chart-options="chartOptions" />
      </section>

      <div class="options-wrapper">
        <div class="title-general">General</div>

        <div class="title">Widget Title</div>
        <BaseInput class="input-title" />

        <div class="title">Widget Description</div>
        <textarea class="description-field" placeholder="Description" />
      </div>
    </div>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import ChartsView from '@/components/widgets/charts/ChartsView'
import BaseInput from '@/components/BaseInput'

export default {
  name: 'ContentVolumeSettingsModal',
  components: {BaseInput, ChartsView, BaseModal},
  props: {
    volume: {
      type: [Array, Object],
      required: true,
    },
  },
  computed: {
    volumeData() {
      return Object.values(this.volume)
    },
    volumeLabels() {
      return this.volumeData.map((el) => this.formatDate(el.date))
    },
    volumeValue() {
      return this.volumeData.map((el) => el.created_count)
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
    formatDate(date) {
      return new Date(date).toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
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

    .input-title {
      margin-bottom: 25px;
    }
  }
}
.description-field {
  width: 475px;
  height: 132px;
  padding: 12px 16px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);

  resize: none;
}
</style>

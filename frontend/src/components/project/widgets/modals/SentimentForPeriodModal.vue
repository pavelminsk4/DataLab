<template>
  <BaseModal modal-frame-style="width: 90vw; height: 80vh;">
    <div class="main-title">{{ sentimentForPeriod.title }}</div>

    <div class="settings-wrapper">
      <section class="chart-wrapper">
        <div class="chart-title">Sentiment For Period</div>
        <LineChart
          v-if="isLineChart"
          :chart-labels="labels"
          :datasets="chartDatasets"
          class="multi-line"
        />
        <PatternsBarChart
          v-else
          :chart-labels="labels"
          :neutral-values="sentiments.neutral"
          :negative-values="sentiments.negative"
          :positive-values="sentiments.positive"
        />
      </section>

      <div class="general-wrapper-settings">
        <SettingsButtons @update-setting-panel="updateSettingPanel" />

        <BasicSettingsScreen
          v-if="panelName === 'General'"
          :period="sentimentForPeriod.aggregation_period"
          :widget-title="sentimentForPeriod.title"
          :widget-description="sentimentForPeriod.description"
          @save-changes="saveChanges"
          @get-widget-params="updateAggregationPeriod"
        />

        <DimensionsScreen
          v-if="panelName === 'Dimensions'"
          :active-dimensions="sentimentForPeriod"
          :project-id="projectId"
          :widget-author="sentimentForPeriod.author_dim_pivot"
          :widget-country="sentimentForPeriod.country_dim_pivot"
          :widget-language="sentimentForPeriod.language_dim_pivot"
          @save-dimensions-settings="saveDimensions"
        />
      </div>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import LineChart from '@/components/project/widgets/charts/LineChart'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'
import PatternsBarChart from '@/components/project/widgets/charts/PatternsBarChart'
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'

export default {
  name: 'SentimentForPeriodModal',
  components: {
    LineChart,
    PatternsBarChart,
    BaseModal,
    SettingsButtons,
    DimensionsScreen,
    BasicSettingsScreen,
  },
  props: {
    sentimentForPeriodValue: {
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
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
    }),
    sentimentForPeriod() {
      return this.widgets['sentiment_for_period_widget']
    },
    labels() {
      let labelsCollection = []

      this.sentimentForPeriodValue.forEach((el) => {
        Object.keys(el).forEach((i) => {
          labelsCollection.push(i)
        })
      })

      return labelsCollection.map((el) => this.formatDate(el))
    },
    sentiments() {
      let neutral = []
      let positive = []
      let negative = []

      this.sentimentForPeriodValue.forEach((el) => {
        Object.values(el).forEach((i) => {
          neutral.push(i.neutral)
          positive.push(i.positive)
          negative.push(i.negative)
        })
      })

      return {
        neutral: [...neutral],
        positive: [...positive],
        negative: [...negative],
      }
    },
    isLineChart() {
      return this.labels?.length > 7
    },
    chartDatasets() {
      return [
        {
          borderColor: '#F6AA37',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#F6AA37',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.neutral,
          skipNull: true,
        },
        {
          borderColor: '#30F47E',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#30F47E',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.positive,
          skipNull: true,
        },
        {
          borderColor: '#F94747',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#F94747',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.negative,
          skipNull: true,
        },
      ]
    },
  },
  methods: {
    ...mapActions([
      action.GET_SENTIMENT_FOR_PERIOD,
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
        this[action.GET_SENTIMENT_FOR_PERIOD]({
          projectId: this.projectId,
          value: {
            smpl_freq: val.toLowerCase(),
            author_dim_pivot: this.sentimentForPeriod.author_dim_pivot || null,
            language_dim_pivot:
              this.sentimentForPeriod.language_dim_pivot || null,
            country_dim_pivot:
              this.sentimentForPeriod.country_dim_pivot || null,
            sentiment_dim_pivot:
              this.sentimentForPeriod.sentiment_dim_pivot || null,
            source_dim_pivot: this.sentimentForPeriod.source_dim_pivot || null,
          },
        })
      } catch (e) {
        console.log(e)
      }
    },
    saveChanges(title, description, aggregationPeriod) {
      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_for_period_widget: {
            id: this.sentimentForPeriod.id,
            title: title || this.sentimentForPeriod.title,
            description: description || this.sentimentForPeriod.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
              this.sentimentForPeriod.aggregation_period,
          },
        },
      })
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    updateSettingPanel(val) {
      this.panelName = val
    },
    saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.sentimentForPeriod.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.sentimentForPeriod.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.sentimentForPeriod.country_dim_pivot
      }

      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_for_period_widget: {
            id: this.sentimentForPeriod.id,
            smpl_freq: this.sentimentForPeriod.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.sentimentForPeriod.sentiment_dim_pivot,
            source_dim_pivot: this.sentimentForPeriod.source_dim_pivot,
          },
        },
      })
      this[action.GET_SENTIMENT_FOR_PERIOD]({
        projectId: this.projectId,
        value: {
          id: this.sentimentForPeriod.id,
          smpl_freq: this.sentimentForPeriod.aggregation_period,
          author_dim_pivot: author,
          language_dim_pivot: language,
          country_dim_pivot: country,
          sentiment_dim_pivot: this.sentimentForPeriod.sentiment_dim_pivot,
          source_dim_pivot: this.sentimentForPeriod.source_dim_pivot,
        },
      })
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
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

  height: 350px;
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

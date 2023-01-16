<template>
  <BaseModal modal-frame-style="width: 90vw; height: 80vh;">
    <div class="main-title">{{ contentVolumeTopAuthorsWidget.title }}</div>

    <div class="settings-wrapper">
      <section class="chart-wrapper">
        <div class="chart-title">{{ contentVolumeTopAuthorsWidget.title }}</div>
        <LineChart :chart-data="chartData" />
      </section>

      <div class="general-wrapper-settings">
        <SettingsButtons @update-setting-panel="updateSettingPanel" />

        <BasicSettingsScreen
          v-if="panelName === 'General'"
          :period="contentVolumeTopAuthorsWidget.aggregation_period"
          :widget-title="contentVolumeTopAuthorsWidget.title"
          :widget-description="contentVolumeTopAuthorsWidget.description"
          @save-changes="saveChanges"
          @get-widget-params="updateAggregationPeriod"
        />

        <DimensionsScreen
          v-if="panelName === 'Dimensions'"
          :active-dimensions="contentVolumeTopAuthorsWidget"
          :project-id="projectId"
          :widget-author="contentVolumeTopAuthorsWidget.author_dim_pivot"
          :widget-country="contentVolumeTopAuthorsWidget.country_dim_pivot"
          :widget-language="contentVolumeTopAuthorsWidget.language_dim_pivot"
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
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'

export default {
  name: 'ContentVolumeTop5AuthorsWidgetModal',
  components: {
    LineChart,
    BaseModal,
    SettingsButtons,
    DimensionsScreen,
    BasicSettingsScreen,
  },
  props: {
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
      contentVolumeTopAuthorsData: get.CONTENT_VOLUME_TOP_AUTHORS,
    }),
    contentVolumeTopAuthorsWidget() {
      return this.widgets['content_volume_top_5_authors_widget']
    },
    labels() {
      let labelsCollection = []
      let keys = []

      Object.values(this.contentVolumeTopAuthorsData).forEach((el) => {
        keys.push(Object.keys(el))
        labelsCollection.push(el[keys[0]])
      })

      return labelsCollection[0]?.map((el) => this.formatDate(el.date))
    },
    chartDatasets() {
      let datasetsValue = []
      let lineColors = [
        '#055FFC',
        '#7A9EF9',
        '#47F9B9',
        '#47F979',
        '#95F947',
        '#F5F947',
        '#F6AA37',
        '#F63737',
        '#F63787',
        '#D930F4',
      ]

      Object.values(this.contentVolumeTopAuthorsData).forEach((el, index) => {
        if (Object.keys(el)[0] === 'Missing in source') {
          datasetsValue.push({
            label: Object.keys(el)[0],
            borderColor: '#808080',
            pointStyle: 'circle',
            pointRadius: 3,
            pointBackgroundColor: '#808080',
            pointBorderWidth: 1,
            pointBorderColor: '#808080',
            borderWidth: 1,
            radius: 0.3,
            fill: true,
            tension: 0.3,
            data: el[Object.keys(el)].map((el) => el.post_count),
            skipNull: true,
            color: '#808080',
          })
        } else {
          datasetsValue.push({
            label: Object.keys(el)[0],
            borderColor: lineColors[index],
            pointStyle: 'circle',
            pointRadius: 3,
            pointBackgroundColor: lineColors[index],
            pointBorderWidth: 1,
            pointBorderColor: '#FFFFFF',
            borderWidth: 1,
            radius: 0.3,
            fill: true,
            tension: 0.3,
            data: el[Object.keys(el)].map((el) => el.post_count),
            skipNull: true,
            color: '#FFFFFF',
          })
        }
      })

      return datasetsValue
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: this.chartDatasets,
      }
    },
  },
  methods: {
    ...mapActions([
      action.GET_CONTENT_VOLUME_TOP_AUTHORS,
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
        this[action.GET_CONTENT_VOLUME_TOP_AUTHORS]({
          projectId: this.projectId,
          value: {
            aggregation_period: val.toLowerCase(),
            author_dim_pivot:
              this.contentVolumeTopAuthorsWidget.author_dim_pivot || null,
            language_dim_pivot:
              this.contentVolumeTopAuthorsWidget.language_dim_pivot || null,
            country_dim_pivot:
              this.contentVolumeTopAuthorsWidget.country_dim_pivot || null,
            sentiment_dim_pivot:
              this.contentVolumeTopAuthorsWidget.sentiment_dim_pivot || null,
            source_dim_pivot:
              this.contentVolumeTopAuthorsWidget.source_dim_pivot || null,
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
          content_volume_top_5_authors_widget: {
            id: this.contentVolumeTopAuthorsWidget.id,
            title: title || this.contentVolumeTopAuthorsWidget.title,
            description:
              description || this.contentVolumeTopAuthorsWidget.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
              this.contentVolumeTopAuthorsWidget.aggregation_period,
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
        author = author || this.contentVolumeTopAuthorsWidget.author_dim_pivot
      }
      if (language || language === '') {
        language =
          language || this.contentVolumeTopAuthorsWidget.language_dim_pivot
      }
      if (country || country === '') {
        country =
          country || this.contentVolumeTopAuthorsWidget.country_dim_pivot
      }

      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          content_volume_top_5_authors_widget: {
            id: this.contentVolumeTopAuthorsWidget.id,
            aggregation_period:
              this.contentVolumeTopAuthorsWidget.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot:
              this.contentVolumeTopAuthorsWidget.sentiment_dim_pivot,
            source_dim_pivot:
              this.contentVolumeTopAuthorsWidget.source_dim_pivot,
          },
        },
      })
      this[action.GET_CONTENT_VOLUME_TOP_AUTHORS]({
        projectId: this.projectId,
        value: {
          id: this.contentVolumeTopAuthorsWidget.id,
          aggregation_period:
            this.contentVolumeTopAuthorsWidget.aggregation_period,
          author_dim_pivot: author,
          language_dim_pivot: language,
          country_dim_pivot: country,
          sentiment_dim_pivot:
            this.contentVolumeTopAuthorsWidget.sentiment_dim_pivot,
          source_dim_pivot: this.contentVolumeTopAuthorsWidget.source_dim_pivot,
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
    border: 1px solid var(--border-color);
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

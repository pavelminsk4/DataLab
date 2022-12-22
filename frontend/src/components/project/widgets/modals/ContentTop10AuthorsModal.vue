<template>
  <BaseModal modal-frame-style="width: 90vw; height: 80vh;">
    <div class="main-title">{{ contentTop10AuthorsWidget.title }}</div>

    <div class="settings-wrapper">
      <section class="chart-wrapper">
        <div class="chart-title">{{ contentTop10AuthorsWidget.title }}</div>
        <LineChart :datasets="chartDatasets" :chart-labels="labels" />
      </section>

      <div class="general-wrapper-settings">
        <SettingsButtons @update-setting-panel="updateSettingPanel" />

        <BasicSettingsScreen
          v-if="panelName === 'General'"
          :period="contentTop10AuthorsWidget.aggregation_period"
          :widget-title="contentTop10AuthorsWidget.title"
          :widget-description="contentTop10AuthorsWidget.description"
          @save-changes="saveChanges"
          @get-widget-params="updateAggregationPeriod"
        />

        <DimensionsScreen
          v-if="panelName === 'Dimensions'"
          :active-dimensions="contentTop10AuthorsWidget"
          :project-id="projectId"
          :widget-author="contentTop10AuthorsWidget.author_dim_pivot"
          :widget-country="contentTop10AuthorsWidget.country_dim_pivot"
          :widget-language="contentTop10AuthorsWidget.language_dim_pivot"
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
  name: 'ContentTop10AuthorsModal',
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
      contentTop10Authors: get.CONTENT_VOLUME_TOP_AUTHORS,
    }),
    contentTop10AuthorsWidget() {
      return this.widgets['content_volume_top_10_authors_widget']
    },
    labels() {
      let labelsCollection = []
      let keys = []

      Object.values(this.contentTop10Authors).forEach((el) => {
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

      Object.values(this.contentTop10Authors).forEach((el, index) => {
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
        })
      })

      return datasetsValue
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
            smpl_freq: val.toLowerCase(),
            author_dim_pivot:
              this.contentTop10AuthorsWidget.author_dim_pivot || null,
            language_dim_pivot:
              this.contentTop10AuthorsWidget.language_dim_pivot || null,
            country_dim_pivot:
              this.contentTop10AuthorsWidget.country_dim_pivot || null,
            sentiment_dim_pivot:
              this.contentTop10AuthorsWidget.sentiment_dim_pivot || null,
            source_dim_pivot:
              this.contentTop10AuthorsWidget.source_dim_pivot || null,
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
          content_volume_top_10_authors_widget: {
            id: this.contentTop10AuthorsWidget.id,
            title: title || this.contentTop10AuthorsWidget.title,
            description:
              description || this.contentTop10AuthorsWidget.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
              this.contentTop10AuthorsWidget.aggregation_period,
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
        author = author || this.contentTop10AuthorsWidget.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.contentTop10AuthorsWidget.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.contentTop10AuthorsWidget.country_dim_pivot
      }

      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          content_volume_top_10_authors_widget: {
            id: this.contentTop10AuthorsWidget.id,
            smpl_freq: this.contentTop10AuthorsWidget.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot:
              this.contentTop10AuthorsWidget.sentiment_dim_pivot,
            source_dim_pivot: this.contentTop10AuthorsWidget.source_dim_pivot,
          },
        },
      })
      this[action.GET_CONTENT_VOLUME_TOP_AUTHORS]({
        projectId: this.projectId,
        value: {
          id: this.contentTop10AuthorsWidget.id,
          smpl_freq: this.contentTop10AuthorsWidget.aggregation_period,
          author_dim_pivot: author,
          language_dim_pivot: language,
          country_dim_pivot: country,
          sentiment_dim_pivot:
            this.contentTop10AuthorsWidget.sentiment_dim_pivot,
          source_dim_pivot: this.contentTop10AuthorsWidget.source_dim_pivot,
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

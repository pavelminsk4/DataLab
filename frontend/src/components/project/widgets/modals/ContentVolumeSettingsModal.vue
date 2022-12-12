<template>
  <BaseModal modal-frame-style="width: 90vw; height: 80vh;">
    <div class="main-title">{{ contentVolumeWidget.title }}</div>

    <div class="settings-wrapper">
      <section class="chart-wrapper">
        <div class="chart-title">Content Volume</div>
        <LineChart
          v-if="isLineChart"
          :chart-values="volumeValue"
          :chart-labels="volumeLabels"
        />
        <BarChart
          v-else
          :chart-values="volumeValue"
          :chart-labels="volumeLabels"
        />
      </section>

      <div class="general-wrapper-settings">
        <SettingsButtons @update-setting-panel="updateSettingPanel" />

        <BasicSettingsScreen
          v-if="panelName === 'General'"
          :period="contentVolumeWidget.aggregation_period"
          :widget-title="contentVolumeWidget.title"
          :widget-description="contentVolumeWidget.description"
          @save-changes="saveChanges"
          @get-widget-params="updateAggregationPeriod"
        />

        <DimensionsScreen
          v-if="panelName === 'Dimensions'"
          :active-dimensions="contentVolumeWidget"
          :project-id="projectId"
          :widget-author="contentVolumeWidget.author_dim_pivot"
          :widget-country="contentVolumeWidget.country_dim_pivot"
          :widget-language="contentVolumeWidget.language_dim_pivot"
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
import BarChart from '@/components/project/widgets/charts/BarChart'
import LineChart from '@/components/project/widgets/charts/LineChart'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'

export default {
  name: 'ContentVolumeSettingsModal',
  components: {
    BarChart,
    LineChart,
    BaseModal,
    SettingsButtons,
    DimensionsScreen,
    BasicSettingsScreen,
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
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
    }),
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
          value: {
            smpl_freq: val.toLowerCase(),
            author_dim_pivot: this.contentVolumeWidget.author_dim_pivot || null,
            language_dim_pivot:
              this.contentVolumeWidget.language_dim_pivot || null,
            country_dim_pivot:
              this.contentVolumeWidget.country_dim_pivot || null,
            sentiment_dim_pivot:
              this.contentVolumeWidget.sentiment_dim_pivot || null,
            source_dim_pivot: this.contentVolumeWidget.source_dim_pivot || null,
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
          volume_widget: {
            id: this.contentVolumeWidget.id,
            title: title || this.contentVolumeWidget.title,
            description: description || this.contentVolumeWidget.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
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
    saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.contentVolumeWidget.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.contentVolumeWidget.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.contentVolumeWidget.country_dim_pivot
      }

      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          volume_widget: {
            id: this.contentVolumeWidget.id,
            smpl_freq: this.contentVolumeWidget.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.contentVolumeWidget.sentiment_dim_pivot,
            source_dim_pivot: this.contentVolumeWidget.source_dim_pivot,
          },
        },
      })
      this[action.GET_VOLUME_WIDGET]({
        projectId: this.projectId,
        value: {
          id: this.contentVolumeWidget.id,
          smpl_freq: this.contentVolumeWidget.aggregation_period,
          author_dim_pivot: author,
          language_dim_pivot: language,
          country_dim_pivot: country,
          sentiment_dim_pivot: this.contentVolumeWidget.sentiment_dim_pivot,
          source_dim_pivot: this.contentVolumeWidget.source_dim_pivot,
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

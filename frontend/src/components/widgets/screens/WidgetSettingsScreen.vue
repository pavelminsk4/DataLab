<template>
  <div class="settings-wrapper">
    <div v-if="widgetDetails.hasPreview" class="preview-section">
      <div class="chart-title">
        {{ widgetDetails.title }}
      </div>

      <slot></slot>
    </div>

    <div class="general-wrapper-settings scroll">
      <BaseTabs
        :main-settings="mainSettings"
        :default-tab="defaultTab"
        @update-setting-panel="updateSettingPanel"
      />

      <BasicSettingsScreen
        v-if="hasBaseSettings"
        :period="widgetDetails.aggregation_period"
        :widget-title="widgetDetails.title"
        :widget-description="widgetDetails.description"
        :hasAggregationPeriod="widgetDetails.hasAggregationPeriod"
        @update-general-data="updateGeneralSettings"
        @change-aggregation-period="changeAggregationPeriod"
      />

      <FiltersScreen
        v-if="hasFilters"
        :module-name="widgetDetails.moduleName"
        :project-id="widgetDetails.projectId"
        :authors-filters="
          widgetDetails.author_dim_pivot || widgetDetails.author_dimensions
        "
        :countries-filters="
          widgetDetails.country_dim_pivot || widgetDetails.country_dimensions
        "
        :languages-filters="
          widgetDetails.language_dim_pivot || widgetDetails.language_dimensions
        "
        :sources-filters="widgetDetails.source_dim_pivot"
        :sentiments-filters="
          widgetDetails.sentiment_dim_pivot ||
          widgetDetails.sentiment_dimensions
        "
        class="dimensions-tab"
      />

      <ChartTypesRadio
        v-if="hasChartLayout"
        :selected="widgetDetails.chart_type || widgetDetails.defaultChartType"
        :widget-name="widgetDetails.name"
        :project-id="widgetDetails.projectId"
        :widget-data="widgetDetails"
        @update-chart-type="$emit('update-chart-type', $event)"
      />

      <BaseButton class="button" @click="saveChanges">
        <SaveIcon />Save
      </BaseButton>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import BaseTabs from '@/components/project/widgets/modals/BaseTabs'
import FiltersScreen from '@/components/project/screens/FiltersScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'
import ChartTypesRadio from '@/components/project/widgets/modals/screens/ChartTypesRadio'
import BaseButton from '@/components/common/BaseButton'
import SaveIcon from '@/components/icons/SaveIcon'

export default {
  name: 'WidgetSettingsScreen',
  components: {
    SaveIcon,
    BaseButton,
    ChartTypesRadio,
    BaseTabs,
    FiltersScreen,
    BasicSettingsScreen,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      panelName: 'General',
      panelNames: ['General', 'لمحة عامة'],
      newWidgetTitle: '',
      newWidgetDescription: '',
      newAggregationPeriod: '',
    }
  },
  computed: {
    ...mapGetters({
      platformLanguage: get.PLATFORM_LANGUAGE,
    }),
    mainSettings() {
      console.log(this.widgetDetails.settingsTabs[this.platformLanguage])
      return this.widgetDetails.settingsTabs[this.platformLanguage]
    },
    defaultTab() {
      return this.widgetDetails.settingsTabs[this.platformLanguage][0]
    },
    hasBaseSettings() {
      return this.panelName === 'General' || this.panelName === 'لمحة عامة'
    },
    hasFilters() {
      return this.panelName === 'Filters' || this.panelName === 'الفلاتر'
    },
    hasChartLayout() {
      return (
        this.panelName === 'Chart Layout' ||
        this.panelName === 'تخطيط الرسم البياني'
      )
    },
  },
  methods: {
    updateSettingPanel(val) {
      this.panelName = val
    },

    updateGeneralSettings(value, optionName) {
      this[optionName] = value
    },

    saveChanges() {
      if (this.panelName === 'General') {
        this.$emit('save-general-settings', {
          newWidgetTitle: this.newWidgetTitle,
          newWidgetDescription: this.newWidgetDescription,
          newAggregationPeriod: this.newAggregationPeriod,
        })
      }
      if (this.panelName === 'Filters') {
        this.$emit('save-filters-settings', '')
      }
      if (this.panelName === 'Chart Layout') {
        this.$emit('save-chart-settings')
      }
    },

    changeAggregationPeriod(aggregationPeriod) {
      this.$emit('change-aggregation-period', aggregationPeriod)
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-wrapper {
  display: flex;

  width: 75vw;
  height: 80vh;

  background-color: var(--background-primary-color);

  .preview-section {
    display: flex;
    flex-direction: column;
    align-items: center;

    width: 58%;
    min-height: 350px;
    height: fit-content;
    margin: 24px;

    .chart-title {
      width: 100%;
      padding: 12px 20px;

      border-bottom: 1px solid var(--border-color);

      font-style: normal;
      font-weight: 500;
      font-size: 18px;
      line-height: 20px;
      color: var(--typography-title-color);
    }

    .widget-view {
      width: 95%;
    }

    box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);
    border-radius: 8px;
    background: var(--background-secondary-color);
  }

  .general-wrapper-settings {
    display: flex;
    flex-direction: column;
    flex: 1;

    padding: 24px;
    height: 100%;

    background-color: var(--background-secondary-color);

    .dimensions-tab {
      margin-top: 35px;
    }

    .button {
      gap: 6px;
      align-self: flex-end;

      width: 84px;
      margin-top: 32px;
    }
  }
}
</style>

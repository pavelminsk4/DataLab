<template>
  <div class="settings-wrapper">
    <div class="preview-section">
      <div class="chart-title">
        {{ generalWidgetData.title }}
      </div>

      <slot></slot>
    </div>

    <div class="general-wrapper-settings">
      <BaseTabs
        :main-settings="settingsTabs"
        default-tab="General"
        @update-setting-panel="updateSettingPanel"
      />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="generalWidgetData.aggregation_period"
        :widget-title="generalWidgetData.title"
        :widget-description="generalWidgetData.description"
        :hasAggregationPeriod="hasAggregationPeriod"
        @update-general-data="updateGeneralSettings"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :project-id="projectId"
        :authors-dimensions="generalWidgetData.author_dim_pivot"
        :countries-dimensions="generalWidgetData.country_dim_pivot"
        :languages-dimensions="generalWidgetData.language_dim_pivot"
        :sources-dimensions="generalWidgetData.source_dim_pivot"
        :sentiments-dimensions="generalWidgetData.sentiment_dim_pivot"
        class="dimensions-tab"
      />

      <ChartTypesRadio
        v-if="panelName === 'Chart Layout'"
        :selected="chartType"
        :widget-name="widgetName"
        :project-id="projectId"
        :widget-data="generalWidgetData"
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
import DimensionsScreen from '@/components/project/screens/DimensionsScreen'
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
    DimensionsScreen,
    BasicSettingsScreen,
  },
  props: {
    widgetData: {type: Object, required: true},
    widgetName: {type: String, required: true},
    projectId: {type: Number, required: true},
    hasAggregationPeriod: {type: Boolean, default: true},
    chartType: {type: String, required: false},
    settingsTabs: {type: Array, required: true},
  },
  data() {
    return {
      panelName: 'General',
      newWidgetTitle: '',
      newWidgetDescription: '',
    }
  },
  computed: {
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
      selectedDimensions: get.SELECTED_DIMENSIONS,
    }),
    generalWidgetData() {
      return this.widgets[this.widgetName]
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
        })
      }
      if (this.panelName === 'Dimensions') {
        this.$emit('save-dimensions-settings', '')
      }
      if (this.panelName === 'Chart Layout') {
        this.$emit('save-chart-settings')
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-wrapper {
  display: flex;

  min-height: 660px;

  background-color: var(--background-primary-color);

  .preview-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex: 1;

    height: fit-content;
    min-height: 300px;
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
    min-height: 100%;

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

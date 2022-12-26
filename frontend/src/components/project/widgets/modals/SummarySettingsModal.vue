<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ summaryWidget.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="summaryWidget.aggregation_period"
        :widget-title="summaryWidget.title"
        :widget-description="summaryWidget.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="summaryWidget"
        :project-id="projectId"
        :widget-author="summaryWidget.author_dim_pivot"
        :widget-country="summaryWidget.country_dim_pivot"
        :widget-language="summaryWidget.language_dim_pivot"
        @save-dimensions-settings="saveDimensions"
      />
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'

export default {
  name: 'SummarySettingsModal',
  components: {
    DimensionsScreen,
    BasicSettingsScreen,
    SettingsButtons,
    BaseModal,
  },
  props: {
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
      panelName: 'General',
    }
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS, loading: get.LOADING}),
    summaryWidget() {
      return this.widgets['summary_widget']
    },
  },
  methods: {
    ...mapActions([
      action.GET_SUMMARY_WIDGET,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          summary_widget: {
            id: this.summaryWidget.id,
            title: this.title || this.summaryWidget.title,
            description: this.description || this.summaryWidget.description,
          },
        },
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
    async saveChanges(title, description, aggregationPeriod) {
      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          summary_widget: {
            id: this.summaryWidget.id,
            title: title || this.summaryWidget.title,
            description: description || this.summaryWidget.description,
            smpl_freq:
              aggregationPeriod.toLowerCase() || this.summaryWidget.smpl_freq,
          },
        },
      })

      await this[action.GET_SUMMARY_WIDGET](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.summaryWidget.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.summaryWidget.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.summaryWidget.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          summary_widget: {
            id: this.summaryWidget.id,
            smpl_freq: this.summaryWidget.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.summaryWidget.sentiment_dim_pivot,
            source_dim_pivot: this.summaryWidget.source_dim_pivot,
          },
        },
      })
      this.loading = true

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_SUMMARY_WIDGET](this.projectId)
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
</style>

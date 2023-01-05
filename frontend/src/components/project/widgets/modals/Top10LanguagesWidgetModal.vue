<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ topLanguages.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="topLanguages.aggregation_period"
        :widget-title="topLanguages.title"
        :widget-description="topLanguages.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="topLanguages"
        :project-id="projectId"
        :widget-author="topLanguages.author_dim_pivot"
        :widget-country="topLanguages.country_dim_pivot"
        :widget-language="topLanguages.language_dim_pivot"
        @save-dimensions-settings="saveDimensions"
      />
    </div>
  </BaseModal>
</template>

<script>
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'
import BaseModal from '@/components/modals/BaseModal'
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

export default {
  name: 'Top10LanguagesWidgetModal',
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
      title: '',
      description: '',
      panelName: 'General',
    }
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS, loading: get.LOADING}),
    topLanguages() {
      return this.widgets['top_10_languages_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_TOP_LANGUAGES_WIDGET,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_languages_widget: {
            id: this.topLanguages.id,
            title: this.title || this.topLanguages.title,
            description: this.description || this.topLanguages.description,
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
          top_10_languages_widget: {
            id: this.topLanguages.id,
            title: title || this.topLanguages.title,
            description: description || this.topLanguages.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
              this.topLanguages.aggregation_period,
          },
        },
      })
      await this[action.GET_TOP_LANGUAGES_WIDGET](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.topLanguages.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.topLanguages.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.topLanguages.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_languages_widget: {
            id: this.topLanguages.id,
            aggregation_period: this.topLanguages.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.topLanguages.sentiment_dim_pivot,
            source_dim_pivot: this.topLanguages.source_dim_pivot,
          },
        },
      })

      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_TOP_LANGUAGES_WIDGET](this.projectId)
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

<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ sentimentTopCountries.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="sentimentTopCountries.aggregation_period"
        :widget-title="sentimentTopCountries.title"
        :widget-description="sentimentTopCountries.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="sentimentTopCountries"
        :project-id="projectId"
        :widget-author="sentimentTopCountries.author_dim_pivot"
        :widget-country="sentimentTopCountries.country_dim_pivot"
        :widget-language="sentimentTopCountries.language_dim_pivot"
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
  name: 'SentimentTop10CountriesWidgetModal',
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
    sentimentTopCountries() {
      return this.widgets['sentiment_top_10_countries_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_SENTIMENT_TOP_COUNTRIES,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_countries_widget: {
            id: this.sentimentTopCountries.id,
            title: this.title || this.sentimentTopCountries.title,
            description:
              this.description || this.sentimentTopCountries.description,
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
          sentiment_top_10_countries_widget: {
            id: this.sentimentTopCountries.id,
            title: title || this.sentimentTopCountries.title,
            description: description || this.sentimentTopCountries.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
              this.sentimentTopCountries.aggregation_period,
          },
        },
      })
      await this[action.GET_SENTIMENT_TOP_COUNTRIES](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.sentimentTopCountries.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.sentimentTopCountries.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.sentimentTopCountries.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_countries_widget: {
            id: this.sentimentTopCountries.id,
            aggregation_period: this.sentimentTopCountries.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.sentimentTopCountries.sentiment_dim_pivot,
            source_dim_pivot: this.sentimentTopCountries.source_dim_pivot,
          },
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_SENTIMENT_TOP_COUNTRIES](this.projectId)
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

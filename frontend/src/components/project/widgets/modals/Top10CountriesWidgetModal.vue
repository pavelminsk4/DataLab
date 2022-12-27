<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ topCountries.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="topCountries.aggregation_period"
        :widget-title="topCountries.title"
        :widget-description="topCountries.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="topCountries"
        :project-id="projectId"
        :widget-author="topCountries.author_dim_pivot"
        :widget-country="topCountries.country_dim_pivot"
        :widget-language="topCountries.language_dim_pivot"
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
  name: 'Top10CountriesWidgetModal',
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
    topCountries() {
      return this.widgets['top_10_countries_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_TOP_BRANDS_WIDGET,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_countries_widget: {
            id: this.topCountries.id,
            title: this.title || this.topCountries.title,
            description: this.description || this.topCountries.description,
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
          top_10_countries_widget: {
            id: this.topCountries.id,
            title: title || this.topCountries.title,
            description: description || this.topCountries.description,
            smpl_freq:
              aggregationPeriod.toLowerCase() || this.topCountries.smpl_freq,
          },
        },
      })
      await this[action.GET_TOP_BRANDS_WIDGET](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.topCountries.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.topCountries.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.topCountries.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_countries_widget: {
            id: this.topCountries.id,
            smpl_freq: this.topCountries.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.topCountries.sentiment_dim_pivot,
            source_dim_pivot: this.topCountries.source_dim_pivot,
          },
        },
      })

      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_TOP_BRANDS_WIDGET](this.projectId)
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

<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ topBrands.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="topBrands.aggregation_period"
        :widget-title="topBrands.title"
        :widget-description="topBrands.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="topBrands"
        :project-id="projectId"
        :widget-author="topBrands.author_dim_pivot"
        :widget-country="topBrands.country_dim_pivot"
        :widget-language="topBrands.language_dim_pivot"
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
  name: 'Top10BrandsWidgetModal',
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
    topBrands() {
      return this.widgets['top_10_brands_widget']
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
          top_10_brands_widget: {
            id: this.topBrands.id,
            title: this.title || this.topBrands.title,
            description: this.description || this.topBrands.description,
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
          top_10_brands_widget: {
            id: this.topBrands.id,
            title: title || this.topBrands.title,
            description: description || this.topBrands.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
              this.topBrands.aggregation_period,
          },
        },
      })
      await this[action.GET_TOP_BRANDS_WIDGET](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.topBrands.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.topBrands.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.topBrands.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_brands_widget: {
            id: this.topBrands.id,
            aggregation_period: this.topBrands.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.topBrands.sentiment_dim_pivot,
            source_dim_pivot: this.topBrands.source_dim_pivot,
          },
        },
      })

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

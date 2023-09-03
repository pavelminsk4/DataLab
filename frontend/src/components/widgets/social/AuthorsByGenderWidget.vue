<template>
  <div class="container">
    <VolumeWidget
      v-bind="$attrs"
      v-if="chartValues.length"
      :widget-details="widgetDetails"
      :labels="labels"
      :chart-values="chartValues"
    />
    <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'
import WidgetsSwitcher from '@/components/layout/WidgetsSwitcher'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'AuthorsByGenderWidget',
  components: {VolumeWidget, WidgetsSwitcher},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      newActiveTab: '',
    }
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    authorsByGender() {
      return (
        this.widgetDetails.widgetData || this.socialWidgets.authorsByGender.data
      )
    },
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
      },
    },
    tabs() {
      return Object.keys(this.authorsByGender)
    },
    currentWidgetData() {
      return this.authorsByGender[this.activeTab]
    },
    labels() {
      if (!this.currentWidgetData) return []
      return this.currentWidgetData.map((el) => el[0] + '')
    },

    chartValues() {
      if (!this.currentWidgetData) return []
      return [
        {
          color: '#516BEE',
          label: this.activeTab,
          data: this.currentWidgetData.map((el) => el[1]),
        },
      ]
    },
    widgetId() {
      return this.socialWidgets.authorsByGender?.id
    },
  },
  created() {
    const hasCurrentData =
      this.authorsByGender.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_AUTHORS_BY_GENDER]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_GENDER]),
  },
}
</script>

<style lang="scss" scoped>
.container {
  flex-direction: column;
  align-items: center;

  width: 100%;
  max-height: 450px;
  height: 100%;
}
</style>

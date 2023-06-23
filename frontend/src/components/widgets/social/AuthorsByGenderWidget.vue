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
      return this.socialWidgets.authorsByGender
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
          data: this.currentWidgetData.map((el) => el[1]),
        },
      ]
    },
  },
  created() {
    if (!this.authorsByGender.length) {
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

  max-height: 450px;
  height: 100%;
}
</style>

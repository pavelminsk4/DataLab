<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    :is-show-delete-btn="false"
    style="--widget-layout-content-padding: 0px"
    class="height-reset top-authors-by-gender-widget"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <OverallTopWidget
      v-for="(widget, index) in widgetData"
      :key="widget.id"
      :widget-data="widget"
      :widget-details="widgetDetails"
      :is-show-delete-btn="false"
      :is-show-settings="false"
      :is-show-settings-btn="false"
      :custom-title="`Overall top authors ${genderTypes[index]}`"
      :table-header="tableHeader"
    />
  </component>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import OverallTopWidget from '@/components/widgets/OverallTopWidget'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'TopAuthorsByGenderWidget',
  components: {OverallTopWidget, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    widgetData() {
      return this.socialWidgets.topAuthorsByGender
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  created() {
    if (!this.widgetData.length) {
      this[action.GET_TOP_AUTHORS_BY_GENDER]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
      this.tableHeader = [
        {name: '', width: '5%'},
        {name: 'Author', width: '15%'},
        {name: 'Gender', width: '15%'},
        {name: 'Media Type', width: '10%'},
        {name: 'Posts', width: '10%'},
        {name: 'Sentiment', width: '25%'},
        {name: 'Reach', width: '10%'},
        {name: 'Engagement', width: '10%'},
      ]
    }
    this.genderTypes = ['male', 'female']
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_BY_GENDER]),
  },
}
</script>

<style lang="scss" scoped>
.height-reset {
  height: fit-content;
}
</style>

<style lang="scss">
.top-authors-by-gender-widget {
  .widget-layout-wrapper {
    border-radius: 0;
  }
}
</style>

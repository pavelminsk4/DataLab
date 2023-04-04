<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
    style="--widget-layout-content-padding: 0px"
    class="height-reset"
  >
    <OverallTopWidget
      v-for="(widget, index) in widgetData"
      :key="widget.id"
      :widget-data="widget"
      :widget-details="widgetDetails"
      :is-show-delete-btn="false"
      :is-show-settings="false"
      :custom-title="`Overall top authors ${genderTypes[index]}`"
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

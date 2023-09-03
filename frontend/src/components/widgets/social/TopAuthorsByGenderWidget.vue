<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    :is-show-delete-btn="false"
    style="--widget-layout-content-padding: 0px"
    class="height-reset top-authors-by-gender-widget widget-table scroll"
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
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.topAuthorsByGender.data
      )
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    widgetId() {
      return this.socialWidgets.topAuthorsByGender?.id
    },
  },
  created() {
    this.tableHeader = [
      {name: '', width: '5%'},
      {name: 'Author', width: '15%', sortProperty: 'name', hasSort: true},
      {name: 'Gender', width: '15%'},
      {name: 'Media Type', width: '10%'},
      {name: 'Posts', width: '10%', sortProperty: 'posts', hasSort: true},
      {name: 'Sentiment', width: '25%'},
      {name: 'Reach', width: '10%', sortProperty: 'reach', hasSort: true},
      {
        name: 'Engagement',
        width: '10%',
        sortProperty: 'engagements',
        hasSort: true,
      },
    ]
    this.genderTypes = ['male', 'female']

    const hasCurrentData =
      this.widgetData.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_TOP_AUTHORS_BY_GENDER]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_BY_GENDER]),
  },
}
</script>

<style lang="scss" scoped>
.widget-table {
  width: 100%;
}

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

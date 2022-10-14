<template>
  <grid-layout
    v-model:layout="layout"
    :col-num="4.5"
    :row-height="30"
    is-draggable
    is-resizable
    vertical-compact
    use-css-transforms
    class="widgets-wrapper"
  >
    <grid-item
      class="widget-item"
      v-for="item in layout"
      :static="item.static"
      :x="item.x"
      :y="item.y"
      :w="item.w"
      :h="item.h"
      :i="item.i"
      :key="item.i"
      :minW="item.minW"
      :minH="item.minH"
      :maxW="item.maxW"
      :maxH="item.maxH"
    >
      <component
        :is="`${item.widgetName}` + 'Widget'"
        :summary-data="summary"
        :volume="volume"
      />
    </grid-item>
  </grid-layout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VueGridLayout from 'vue3-grid-layout'
import SummaryWidget from '@/components/widgets/SummaryWidget'
import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'
import VolumeLineWidget from '@/components/widgets/VolumeLineWidget'
import BarWidget from '@/components/widgets/BarWidget'

export default {
  name: 'WidgetsView',
  components: {
    SummaryWidget,
    ContentVolumeWidget,
    VolumeLineWidget,
    BarWidget,
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
  },
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      layout: [
        {
          x: 0,
          y: 0,
          w: 2,
          h: 6,
          i: '0',
          static: false,
          minW: 1.3,
          minH: 6,
          maxW: 2,
          maxH: 6,
          widgetName: 'Summary',
        },
        {
          x: 0,
          y: 1,
          w: 2,
          h: 10,
          i: '1',
          static: false,
          minW: 2,
          minH: 5,
          maxW: 2,
          maxH: 6,
          widgetName: 'ContentVolume',
        },
        {
          x: 2,
          y: 3,
          w: 2,
          h: 10,
          i: '2',
          static: false,
          minW: 2,
          minH: 5,
          maxW: 2,
          maxH: 6,
          widgetName: 'VolumeLine',
        },
        {
          x: 2,
          y: 3,
          w: 2,
          h: 10,
          i: '3',
          static: false,
          minW: 2,
          minH: 5,
          maxW: 2,
          maxH: 6,
          widgetName: 'Bar',
        },
      ],
    }
  },
  created() {
    this[action.GET_SUMMARY_WIDGET](this.projectId)
    this[action.GET_VOLUME_WIDGET](this.projectId)
  },
  computed: {
    ...mapGetters({summary: get.SUMMARY_WIDGET, volume: get.VOLUME_WIDGET}),
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGET, action.GET_VOLUME_WIDGET]),
  },
}
</script>

<style lang="scss" scoped>
.widgets-wrapper {
  margin-top: 30px;

  .widget-item {
    border-radius: 8px;
    border: 1px solid var(--input-border-color);
    background-color: var(--secondary-bg-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);

    color: var(--primary-text-color);
  }
}
</style>

<style>
.vue-grid-layout {
  margin-left: -10px;
}

.vue-grid-item.vue-grid-placeholder {
  border-radius: 8px;
  border: 1px solid var(--input-border-color);
  background: var(--secondary-text-color);
}

.vue-resizable-handle {
  background: var(--secondary-text-color);
}
</style>

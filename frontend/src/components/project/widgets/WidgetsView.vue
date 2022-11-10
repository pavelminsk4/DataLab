<template>
  <ContentVolumeSettingsModal
    v-if="isOpenContentVolumeModal"
    @close="openModal('isOpenContentVolumeModal')"
    :volume="volume"
    :project-id="projectId"
  />

  <SummaryModal
    v-if="isOpenSummaryModal"
    :project-id="projectId"
    @close="openModal('isOpenSummaryModal')"
  />

  <TopAuthorsSettingsModal
    v-if="isOpenTop10AuthorsModal"
    :project-id="projectId"
    @close="openModal('isOpenTop10AuthorsModal')"
  />

  <grid-layout
    v-if="availableWidgets"
    v-model:layout="layout"
    :col-num="4"
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
      v-show="item.isShow"
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
        :project-id="projectId"
        :is-open-widget="item.isShow"
        @delete-widget="deleteWidget(item.name)"
        @open-content-volume-modal="openModal(item.isOpenModal)"
        @open-summary-modal="openModal(item.isOpenModal)"
      />
    </grid-item>
  </grid-layout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VueGridLayout from 'vue3-grid-layout'
import SummaryWidget from '@/components/project/widgets/SummaryWidget'
import ContentVolumeWidget from '@/components/project/widgets/ContentVolumeWidget'
import ClippingFeedContentWidget from '@/components/project/widgets/ClippingFeedContentWidget'
import Top10AuthorsByVolumeWidget from '@/components/project/widgets/Top10AuthorsByVolumeWidget'

import TopAuthorsSettingsModal from '@/components/project/widgets/modals/TopAuthorsSettingsModal'
import ContentVolumeSettingsModal from '@/components/project/widgets/modals/ContentVolumeSettingsModal'
import SummaryModal from '@/components/project/widgets/modals/SummarySettingsModal'

export default {
  name: 'WidgetsView',
  components: {
    SummaryModal,
    ClippingFeedContentWidget,
    ContentVolumeSettingsModal,
    TopAuthorsSettingsModal,
    SummaryWidget,
    ContentVolumeWidget,
    Top10AuthorsByVolumeWidget,
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
      isOpenContentVolumeModal: false,
      isOpenSummaryModal: false,
      isOpenTop10AuthorsModal: false,
    }
  },
  created() {
    this[action.GET_AVAILABLE_WIDGETS](this.projectId)
  },
  computed: {
    ...mapGetters({
      summary: get.SUMMARY_WIDGET,
      volume: get.VOLUME_WIDGET,
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    layout() {
      return [
        {
          x: 0,
          y: 0,
          w: 2,
          h: 9,
          i: '0',
          static: false,
          name: 'summary_widget',
          widgetName: 'Summary',
          isShow: this.isActiveWidget('summary_widget'),
          isOpenModal: 'isOpenSummaryModal',
        },
        {
          x: 2,
          y: 1,
          w: 2,
          h: 12,
          i: '1',
          static: false,
          name: 'volume_widget',
          widgetName: 'ContentVolume',
          isShow: this.isActiveWidget('volume_widget'),
          isOpenModal: 'isOpenContentVolumeModal',
        },
        {
          x: 2,
          y: 1,
          w: 2,
          h: 15,
          i: '2',
          static: false,
          name: 'clipping_feed_content_widget',
          widgetName: 'ClippingFeedContent',
          isShow: this.isActiveWidget('clipping_feed_content_widget'),
        },
        {
          x: 0,
          y: 1,
          w: 2,
          h: 11,
          maxW: 2,
          minW: 2,
          maxH: 11,
          minH: 11,
          i: '3',
          static: false,
          name: 'top_10_authors_by_volume_widget',
          widgetName: 'Top10AuthorsByVolume',
          isShow: this.isActiveWidget('top_10_authors_by_volume_widget'),
          isOpenModal: 'isOpenTop10AuthorsModal',
        },
      ]
    },
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
    async deleteWidget(name) {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {[name]: {is_active: false, id: this.availableWidgets[name].id}},
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    },
    isActiveWidget(key) {
      return this.availableWidgets[key]?.is_active
    },
    openModal(val) {
      this[val] = !this[val]
    },
  },
}
</script>

<style lang="scss" scoped>
.widgets-wrapper {
  min-width: 100%;
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

<template>
  <ContentVolumeSettingsModal
    v-if="isOpenContentVolumeModal"
    @close="openModal('isOpenContentVolumeModal')"
    :volume="volume"
    :project-id="projectId"
  />

  <SummarySettingsModal
    v-if="isOpenSummaryModal"
    :project-id="projectId"
    @close="openModal('isOpenSummaryModal')"
  />

  <TopAuthorsSettingsModal
    v-if="isOpenTop10AuthorsModal"
    :project-id="projectId"
    @close="openModal('isOpenTop10AuthorsModal')"
  />

  <TopBrandsSettingsModal
    v-if="isOpenTopBrandsModal"
    :project-id="projectId"
    @close="openModal('isOpenTopBrandsModal')"
  />

  <ClippingFeedContentModal
    v-if="isOpenClippingFeedContentModal"
    :project-id="projectId"
    @close="openModal('isOpenClippingFeedContentModal')"
  />

  <grid-layout
    v-if="availableWidgets"
    v-model:layout="layoutProxy"
    :col-num="4"
    :row-height="30"
    :is-resizable="false"
    is-draggable
    vertical-compact
    use-css-transforms
    class="widgets-wrapper"
  >
    <grid-item
      class="widget-item"
      v-for="item in layoutProxy"
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
        v-if="item.isWidget"
        :is="`${item.widgetName}` + 'Widget'"
        :summary-data="summary"
        :volume="volume"
        :project-id="projectId"
        :is-open-widget="item.isShow"
        :current-project="currentProject"
        @delete-widget="deleteWidget(item.name, item.i)"
        @open-settings-modal="openModal(item.isOpenModal)"
      />

      <SearchResults
        v-else
        :is-show-calendar="false"
        :is-checkbox-clipping-widget="true"
        :currentProject="currentProject"
        :clipping-content="clippingData"
        @update-page="updatePage"
        @update-posts-count="updatePosts"
      />
    </grid-item>
  </grid-layout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VueGridLayout from 'vue3-grid-layout'
import SearchResults from '@/components/SearchResults'
import SummaryWidget from '@/components/project/widgets/SummaryWidget'
import ContentVolumeWidget from '@/components/project/widgets/ContentVolumeWidget'
import ClippingFeedContentWidget from '@/components/project/widgets/ClippingFeedContentWidget'
import Top10BrandsWidget from '@/components/project/widgets/Top10BrandsWidget'
import Top10AuthorsByVolumeWidget from '@/components/project/widgets/Top10AuthorsByVolumeWidget'

import TopAuthorsSettingsModal from '@/components/project/widgets/modals/TopAuthorsSettingsModal'
import ContentVolumeSettingsModal from '@/components/project/widgets/modals/ContentVolumeSettingsModal'
import SummarySettingsModal from '@/components/project/widgets/modals/SummarySettingsModal'
import ClippingFeedContentModal from '@/components/project/widgets/modals/ClippingFeedContentModal'
import TopBrandsSettingsModal from '@/components/project/widgets/modals/TopBrandsSettingsModal'

export default {
  name: 'WidgetsView',
  components: {
    TopBrandsSettingsModal,
    ClippingFeedContentModal,
    SearchResults,
    SummarySettingsModal,
    ClippingFeedContentWidget,
    ContentVolumeSettingsModal,
    TopAuthorsSettingsModal,
    SummaryWidget,
    ContentVolumeWidget,
    Top10BrandsWidget,
    Top10AuthorsByVolumeWidget,
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
  },
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  emits: ['update-page', 'update-posts-count'],
  data() {
    return {
      isOpenContentVolumeModal: false,
      isOpenSummaryModal: false,
      isOpenTop10AuthorsModal: false,
      isOpenClippingFeedContentModal: false,
      isOpenTopBrandsModal: false,
      layout: [],
    }
  },
  created() {
    if (!this.availableWidgets) {
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    }

    if (!this.clippingData.length) {
      this[action.GET_CLIPPING_FEED_CONTENT_WIDGET](this.projectId)
    }
  },
  computed: {
    ...mapGetters({
      summary: get.SUMMARY_WIDGET,
      volume: get.VOLUME_WIDGET,
      availableWidgets: get.AVAILABLE_WIDGETS,
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
    layoutProxy: {
      get() {
        let layout = [
          {
            x: 0,
            y: 0,
            w: 2,
            h: 29,
            i: '10',
            static: false,
            name: 'search',
            widgetName: 'search',
            isShow: true,
            isOpenModal: 'search',
            isWidget: false,
          },
        ]

        for (let key in this.availableWidgets) {
          if (this.availableWidgets[key].is_active) {
            layout.push({
              x: 2,
              y: this.newValue(layout.length),
              w: 2,
              h: this.widgetSettings(key).h,
              i: this.elementIndex(layout.length),
              static: false,
              name: key,
              widgetName: this.widgetSettings(key).name,
              isShow: this.isActiveWidget(key),
              isOpenModal: this.widgetSettings(key).openModal,
              isWidget: true,
            })
          }
        }

        return layout
      },
      set(val) {
        this.layout = val
      },
    },
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
    widgetSettings(key) {
      switch (key) {
        case 'summary_widget':
          return {
            name: 'Summary',
            openModal: 'isOpenSummaryModal',
            h: 9,
          }
        case 'clipping_feed_content_widget':
          return {
            name: 'ClippingFeedContent',
            openModal: 'isOpenClippingFeedContentModal',
            h: 15,
          }
        case 'top_10_authors_by_volume_widget':
          return {
            name: 'Top10AuthorsByVolume',
            openModal: 'isOpenTop10AuthorsModal',
            h: 11,
          }
        case 'volume_widget':
          return {
            name: 'ContentVolume',
            openModal: 'isOpenContentVolumeModal',
            h: 12,
          }
        case 'top_10_brands_widget':
          return {
            name: 'Top10Brands',
            openModal: 'isOpenTopBrandsModal',
            h: 11,
          }
      }
    },
    newValue(val) {
      return val > 1 ? val - 1 : 0
    },
    elementIndex(val) {
      let index = val + 1
      return String(index)
    },
    async deleteWidget(name, val) {
      const index = this.layout.map((item) => item.i).indexOf(val)
      this.layout.splice(index, 1)

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {[name]: {is_active: false, id: this.availableWidgets[name].id}},
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    },
    updatePage(page, posts) {
      this.$emit('update-page', page, posts)
    },
    updatePosts(page, posts) {
      this.$emit('update-posts-count', page, posts)
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
  background: var(--secondary-text-color) !important;
}
.search-result-wrapper {
  padding: 20px;
}
</style>

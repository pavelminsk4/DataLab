<template>
  <BaseModal modal-frame-style="width:90vw;">
    <template #title>
      Top Results
      <div class="hint">{{ allAvailablePosts }} results</div>
    </template>

    <BaseSpinner v-if="loading" />

    <div v-else class="interactive-modal-wrapper">
      <BaseTabs :main-settings="tabs" default-tab="Top Results" class="tabs" />

      <div class="cards">
        <ClippingCard
          v-for="(item, index) in posts"
          :key="'result' + index"
          :id="item.id"
          :img="cardImg(item)"
          :title="item.entry_title"
          :country="item.feedlink__country"
          :entry-link="item.entry_links_href"
          :summary="item.entry_summary"
          :sentiment="item.sentiment"
          :published="item.entry_published"
          :source-link="item.feedlink__sourceurl"
          :source="item.feedlink__source1"
          :language="item.feed_language__language"
          :potential-reach="item.feedlink__alexaglobalrank"
          :widget-id="widgetId"
          :currentProject="currentProject"
          class="clipping-card"
        />
      </div>
    </div>

    <div class="pagination">
      <PaginationTabs
        v-model="currentPage"
        :pages="12"
        :posts-on-page="postsOnPage"
        :new-count-posts="countPosts"
        @update-page="pageChange"
        @update-posts-count="updatePostsCount"
      />
    </div>
  </BaseModal>
</template>

<script>
import {mapGetters, mapState} from 'vuex'
import {get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import ClippingCard from '@/components/ClippingCard'
import BaseSpinner from '@/components/BaseSpinner'
import BaseTabs from '@/components/project/widgets/modals/BaseTabs'
import PaginationTabs from '@/components/PaginationTabs'

export default {
  name: 'InteractiveWidgetModal',
  components: {PaginationTabs, BaseTabs, BaseSpinner, ClippingCard, BaseModal},
  props: {
    widgetId: {
      type: Number,
      required: true,
    },
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  data() {
    return {
      currentPage: 1,
      countPosts: 4,
      postsOnPage: [4, 8, 16],
      tabs: ['Top Results'],
    }
  },
  computed: {
    ...mapState(['loading']),
    ...mapGetters({
      interactiveWidgets: get.INTERACTIVE_DATA,
    }),
    posts() {
      return this.interactiveWidgets.posts
    },
    allAvailablePosts() {
      return this.interactiveWidgets.num_posts
    },
    numberOfPages() {
      return this.interactiveWidgets.num_pages
    },
  },
  methods: {
    cardImg(item) {
      let images = [
        item.entry_media_content_url,
        item.entry_media_thumbnail_url,
        item.feed_image_href,
        item.feed_image_link,
      ]
      return images.filter((el) => el !== 'None')[0] || 'None'
    },
    updatePostsCount(page, countPosts) {
      this.countPosts = countPosts
      this.$emit('update-posts-count', page, countPosts)
    },
    pageChange(page) {
      this.$emit('update-page', page, this.countPosts)
    },
  },
}
</script>

<style lang="scss" scoped>
.hint {
  margin-left: 12px;

  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-secondary-color);
}

.tabs {
  width: 100%;
  margin-bottom: 25px;
}

.interactive-modal-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  height: 100%;

  .cards {
    display: flex;
    flex-wrap: wrap;
    gap: 32px;

    .clipping-card {
      flex: 1;
    }
  }
}

.pagination {
  display: flex;
  flex-direction: row;
  gap: 18px;

  margin-top: 20px;
}
</style>

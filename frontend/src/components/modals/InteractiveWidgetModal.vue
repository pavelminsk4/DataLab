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
        <component
          :is="postCard"
          v-for="(item, index) in posts"
          :key="'result' + index"
          :img="cardImg(item)"
          :post-details="item"
          class="clipping-card"
        />
      </div>
    </div>

    <div class="pagination">
      <PaginationControlPanel
        v-if="numberOfPages"
        v-model="currentPage"
        :pages="numberOfPages"
        :posts-on-page="postsOnPage"
        :count-posts="countPosts"
        @update-page="updatePage"
      />
    </div>
  </BaseModal>
</template>

<script>
import {mapGetters, mapState} from 'vuex'
import {get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import BaseSpinner from '@/components/BaseSpinner'
import OnlinePostCard from '@/components/OnlinePostCard'
import SocialPostCard from '@/components/SocialPostCard'
import BaseTabs from '@/components/project/widgets/modals/BaseTabs'
import PaginationControlPanel from '@/components/PaginationControlPanel'

export default {
  name: 'InteractiveWidgetModal',
  components: {
    PaginationControlPanel,
    BaseTabs,
    BaseSpinner,
    BaseModal,
    OnlinePostCard,
    SocialPostCard,
  },
  props: {
    widgetId: {type: Number, required: false},
    currentProject: {type: [Array, Object], required: true},
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
    postCard() {
      return this.currentProject.source + 'PostCard'
    },
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
    updatePage(page, countPosts) {
      this.countPosts = countPosts
      this.$emit('show-results', page, countPosts)
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

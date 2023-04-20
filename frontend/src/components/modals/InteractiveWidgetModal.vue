<template>
  <BaseModal modal-frame-style="width:90vw;">
    <template #title>
      Top Results
      <div class="hint">{{ allAvailablePosts }} results</div>
    </template>

    <BaseSpinner v-if="loading" />

    <div v-else class="interactive-modal-wrapper">
      <BaseTabs :main-settings="tabs" default-tab="Top Results" class="tabs" />

      <div class="settings-panel">
        <div class="results">{{ allAvailablePosts }} results</div>

        <component
          v-for="(item, index) in displayTypes"
          :key="item + index"
          :is="item + 'Icon'"
          :class="[
            'display-type',
            postsDisplayType === item.toLowerCase() && 'active-type',
          ]"
          @click="updateDisplayType(item)"
        />
      </div>

      <div :class="[postsDisplayType]">
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
import NormalIcon from '@/components/icons/PostsDisplayNormalIcon.vue'
import CompactIcon from '@/components/icons/PostsDisplayCompactIcon.vue'

export default {
  name: 'InteractiveWidgetModal',
  components: {
    PaginationControlPanel,
    BaseTabs,
    BaseSpinner,
    BaseModal,
    OnlinePostCard,
    SocialPostCard,
    NormalIcon,
    CompactIcon,
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
      displayTypes: ['Normal', 'Compact'],
      postsDisplayType: 'normal',
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
    updateDisplayType(type) {
      this.postsDisplayType = type.toLowerCase()
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
}

.interactive-modal-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  height: 100%;

  .settings-panel {
    display: flex;
    justify-content: flex-end;
    align-items: center;

    width: 100%;
    margin: 30px 0 25px 0;

    .results {
      margin-right: 40px;

      font-style: normal;
      font-weight: 600;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-primary-color);
    }

    .active-type {
      border: 1px solid var(--primary-color);
      background-color: var(--primary-active-color);

      color: var(--primary-color);
    }

    .display-type {
      width: 36px;
      height: 36px;
      padding: 10px;
      margin-right: 12px;

      border-radius: 4px;
      background-color: var(--background-primary-color);

      cursor: pointer;

      &:last-child {
        margin-right: 0;
      }
    }
  }

  .normal {
    display: flex;
    flex-direction: column;
  }

  .compact {
    display: grid;
    grid-gap: 32px;
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: 300px;
  }
}

.pagination {
  display: flex;
  flex-direction: row;
  gap: 18px;

  margin-top: 20px;
}
</style>

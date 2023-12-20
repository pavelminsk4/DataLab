<template>
  <BaseModal modal-frame-style="width:90vw;">
    <template #title>
      <CustomText text="Top Results" />
      <CustomText :text="`${allAvailablePosts} results`" class="hint" />
    </template>

    <BaseSpinner v-if="loading" />

    <div v-else class="interactive-modal-wrapper">
      <div class="settings-panel">
        <CustomText :text="`${allAvailablePosts} results`" class="results" />

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

      <NoPostsIcon v-if="!loading && !posts.length" />
      <div v-if="!loading && !posts.length" class="no-posts">
        <CustomText text="No posts here" />
        &#128531;
      </div>

      <div :class="[postsDisplayType]">
        <component
          :is="postCard"
          v-for="(item, index) in posts"
          :key="'result' + index"
          :img="cardImg(item)"
          :post-details="item"
          :is-clipping-post="isClippingPost(item.id)"
          class="clipping-card"
          @update-interactive-data="updateInteractiveData"
        />
      </div>
    </div>

    <div class="pagination">
      <PaginationControlPanel
        v-if="numberOfPages && posts.length"
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
import {mapGetters, mapState, mapActions} from 'vuex'
import {get, action} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

import CustomText from '@components/CustomText'
import BaseModal from '@components/modals/BaseModal'
import BaseSpinner from '@components/BaseSpinner'
import OnlinePostCard from '@components/OnlinePostCard'
import SocialPostCard from '@components/SocialPostCard'
import AccountAnalysisPostCard from '@components/SocialPostCard'
import PaginationControlPanel from '@components/PaginationControlPanel'
import NormalIcon from '@components/icons/PostsDisplayNormalIcon'
import CompactIcon from '@components/icons/PostsDisplayCompactIcon'
import NoPostsIcon from '@components/icons/NoPostsIcon'

export default {
  name: 'InteractiveWidgetModal',
  components: {
    PaginationControlPanel,
    BaseSpinner,
    BaseModal,
    OnlinePostCard,
    SocialPostCard,
    AccountAnalysisPostCard,
    NormalIcon,
    CompactIcon,
    NoPostsIcon,
    CustomText,
  },
  props: {
    widgetId: {type: Number, required: false},
    moduleName: {type: String, required: false},
    widgetDetails: {type: Object, required: false},
    currentProject: {type: [Array, Object], required: true},
    clippingContent: {type: [Array, Object], default: () => []},
  },
  data() {
    return {
      currentPage: 1,
      countPosts: 4,
      postsOnPage: [4, 8, 16],
      displayTypes: ['Normal', 'Compact'],
      postsDisplayType: 'normal',
    }
  },
  computed: {
    ...mapState(['loading']),
    ...mapGetters({
      interactiveWidgets: get.INTERACTIVE_DATA,
      inreractiveDataModal: get.INTERACTIVE_DATA_MODAL,
    }),
    postCard() {
      if (this.moduleName === 'Comparison')
        return capitalizeFirstLetter(this.widgetDetails.module) + 'PostCard'
      if (this.moduleName === 'AccountAnalysis')
        return 'AccountAnalysisPostCard'
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
    ...mapActions([action.UPDATE_INTERACTIVE_DATA]),
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
    isClippingPost(id) {
      return this.clippingContent.some((el) => el.post__id === id)
    },
    updateInteractiveData() {
      this[action.UPDATE_INTERACTIVE_DATA](true)
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

.interactive-modal-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  height: 100%;

  .no-posts {
    display: flex;

    margin-top: 20px;

    font-size: 18px;
    font-weight: 500;
  }

  .settings-panel {
    display: flex;
    justify-content: flex-end;
    align-items: center;

    width: 100%;
    margin: 0 0 25px 0;

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

    width: 100%;
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

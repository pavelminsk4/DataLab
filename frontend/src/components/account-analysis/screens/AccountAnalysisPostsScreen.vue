<template>
  <section class="container">
    <section class="filters">
      <!-- <div class="filters__input">
        <BaseInput
          v-model="searchText"
          :isSearch="true"
          placeholder="Search posts..."
          label=" "
        />
      </div> -->
    </section>
    <section v-if="findedposts.length">
      <component :is="`${currentTab}PostsLayout`" :posts="findedposts" />
      <div class="pagination-wrapper">
        <PaginationControlPanel
          v-model="currentPage"
          :pages="numberOfPages"
          :posts-on-page="postsOnPage"
          :count-posts="countPosts"
          @update-page="updatePage"
        />
      </div>
    </section>

    <section v-else class="no-posts">
      <img src="@assets/account-analysis/no-posts.svg" alt="No posts image" />
      <CustomText tag="span" text="No posts here" />&#128532;
    </section>
  </section>
</template>

<script>
import {action} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
// import BaseInput from '@components/common/BaseInput'
import PaginationControlPanel from '@components/PaginationControlPanel'
import CustomText from '@components/CustomText'
import AccountActivityPostsLayout from '@components/account-analysis/AccountActivityPostsLayout'
import MentionsPostsLayout from '@components/account-analysis/MentionsPostsLayout'

const {mapState: mapStateAccountAnalysis, mapActions} =
  createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisPostsScreen',
  components: {
    // BaseInput,
    PaginationControlPanel,
    AccountActivityPostsLayout,
    MentionsPostsLayout,
    CustomText,
  },
  props: {
    currentProject: {type: Object, required: true},
    currentTab: {type: String, required: true},
  },
  data() {
    return {
      currentPage: 1,
      countPosts: 20,
      searchText: '',
      postsOnPage: [20, 50, 100],
      numberOfPages: 0,
    }
  },
  computed: {
    ...mapStateAccountAnalysis(['accountActivityPosts', 'mentionsPosts']),
    findedposts() {
      const currentPosts =
        this.currentTab === 'Mentions'
          ? this.mentionsPosts
          : this.accountActivityPosts
      return currentPosts.filter((post) => post.text.includes(this.searchText))
    },
  },
  created() {
    if (!this.accountActivityPosts.length || !this.mentionsPosts.length) {
      this.getPosts(this.currentPage, this.countPosts)
    }
  },
  methods: {
    ...mapActions([
      action.GET_ACCOUNT_ACTIVITY_POSTS,
      action.GET_MENTIONS_POSTS,
    ]),
    async getPosts(page, countPosts) {
      const actionName =
        this.currentTab === 'Mentions' ? 'MENTIONS' : 'ACCOUNT_ACTIVITY'

      const response = await this[action[`GET_${actionName}_POSTS`]]({
        projectId: this.currentProject.id,
        value: {posts_per_page: countPosts, page_number: page},
      })

      this.numberOfPages = response.num_pages
    },
    updatePage(page, countPosts) {
      this.countPosts = countPosts
      this.getPosts(page, countPosts)
    },
  },
  watch: {
    currentTab() {
      this.currentPage = 1
      this.getPosts(this.currentPage, this.countPosts)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;

  gap: 20px;

  cursor: default;

  .filters {
    display: flex;

    gap: 40px;

    &__sort {
      display: flex;
      align-items: center;

      gap: 15px;
    }

    &__input {
      width: 320px;
    }
  }

  .pagination-wrapper {
    display: flex;
    justify-content: flex-end;
    gap: 18px;

    padding: 15px 32px;
    width: 100%;

    border: 1px solid var(--input-border-color);
    background-color: var(--background-primary-color);
  }

  .no-posts {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    padding-bottom: 55px;
  }
}
</style>

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
      <img src="@/assets/account-analysis/no-posts.svg" alt="No posts image" />
      <span> No posts here&#128532;</span>
    </section>
  </section>
</template>

<script>
import {action} from '@store/constants'
import {createNamespacedHelpers, mapState} from 'vuex'
// import BaseInput from '@/components/common/BaseInput'
import PaginationControlPanel from '@/components/PaginationControlPanel'
import AccountActivityPostsLayout from '@/components/account-analysis/AccountActivityPostsLayout'

const {mapState: mapStateAccountAnalysis, mapActions} =
  createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisPostsScreen',
  components: {
    // BaseInput,
    PaginationControlPanel,
    AccountActivityPostsLayout,
  },
  props: {
    currentProject: {type: Object, required: true},
    currentTab: {type: String, required: true},
  },
  data() {
    return {
      searchText: '',
      currentPage: 1,
      countPosts: 20,
      postsOnPage: [20, 50, 100],
    }
  },
  computed: {
    ...mapStateAccountAnalysis(['accountActivityPosts', 'mentionsPosts']),
    ...mapState(['numberOfPages']),
    findedposts() {
      const currentPosts =
        this.currentTab === 'Mentions'
          ? this.mentionsPosts
          : this.accountActivityPosts
      return currentPosts.filter((post) => post.text.includes(this.searchText))
    },
  },
  created() {
    this.checkForPosts()
  },
  methods: {
    ...mapActions([
      action.GET_ACCOUNT_ACTIVITY_POSTS,
      action.GET_MENTIONS_POSTS,
    ]),
    getPosts(page, countPosts) {
      const actionName =
        this.currentTab === 'Mentions' ? 'MENTIONS' : 'ACCOUNT_ACTIVITY'
      console.log(this.currentPage, page)
      this[action[`GET_${actionName}_POSTS`]]({
        projectId: this.currentProject.id,
        value: {posts_per_page: countPosts, page_number: page},
      })
    },
    updatePage(page, countPosts) {
      this.countPosts = countPosts
      this.getPosts(page, countPosts)
    },
    checkForPosts() {
      if (
        !this.accountActivityPosts.length &&
        this.currentTab === 'AccountActivity'
      ) {
        this.getPosts(this.currentPage, this.countPosts)
      }

      if (!this.mentionsPosts.length && this.currentTab === 'Mentions') {
        this.getPosts(this.currentPage, this.countPosts)
      }
    },
  },
  watch: {
    currentTab() {
      this.checkForPosts()
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
    position: absolute;
    bottom: 0;
    right: 0;

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

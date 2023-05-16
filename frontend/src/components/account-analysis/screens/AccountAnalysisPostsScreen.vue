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
    <section class="posts">
      <AccountAnalysisPostCard
        v-for="post in findedposts"
        :post-details="post"
        :key="post.id"
      />
    </section>

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
</template>

<script>
import {action} from '@store/constants'
import {createNamespacedHelpers, mapState} from 'vuex'

import AccountAnalysisPostCard from '@/components/account-analysis/AccountAnalysisPostCard'
// import BaseInput from '@/components/common/BaseInput'
import PaginationControlPanel from '@/components/PaginationControlPanel'

const {mapState: mapStateAccountAnalysis, mapActions} =
  createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisPostsScreen',
  components: {
    AccountAnalysisPostCard,
    // BaseInput,
    PaginationControlPanel,
  },
  props: {
    currentProject: {type: Object, required: true},
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
    ...mapStateAccountAnalysis(['posts']),
    ...mapState(['numberOfPages']),
    findedposts() {
      return this.posts.filter((post) => post.text.includes(this.searchText))
    },
  },
  created() {
    if (!this.posts.length) {
      this.getPosts(this.currentPage, this.countPosts)
    }
  },
  methods: {
    ...mapActions([action.GET_POSTS]),
    getPosts(page, countPosts) {
      this[action.GET_POSTS]({
        projectId: this.currentProject.id,
        value: {posts_per_page: countPosts, page_number: page},
      })
    },
    updatePage(page, countPosts) {
      this.countPosts = countPosts
      this.getPosts(page, countPosts)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;

  gap: 20px;

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

  .posts {
    display: grid;
    grid-template-columns: 45% 2fr;

    gap: 50px;
    margin-bottom: 50px;
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
}
</style>

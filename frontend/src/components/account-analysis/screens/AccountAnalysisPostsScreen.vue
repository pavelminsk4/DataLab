<template>
  <section class="container">
    <section class="filters">
      <!-- <div class="filters__sort">
        <span> Sort by </span>
        <div>Date^</div>
      </div> -->
      <div class="filters__input">
        <BaseInput
          v-model="searchText"
          :isSearch="true"
          placeholder="Search posts..."
          label=" "
        />
      </div>
    </section>
    <section class="posts">
      <AccountAnalysisPostCard
        v-for="post in findedposts"
        :post-details="post"
        :key="post.id"
      />
    </section>
  </section>
</template>

<script>
import {action} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'

import AccountAnalysisPostCard from '@/components/account-analysis/AccountAnalysisPostCard'
import BaseInput from '@/components/common/BaseInput'

const {mapState, mapActions} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisPostsScreen',
  components: {AccountAnalysisPostCard, BaseInput},
  props: {
    currentProject: {type: Object, required: true},
  },
  data() {
    return {
      searchText: '',
    }
  },
  computed: {
    ...mapState(['posts']),
    findedposts() {
      return this.posts.filter((post) => post.text.includes(this.searchText))
    },
  },
  created() {
    if (!this.posts.length) {
      this[action.GET_POSTS](this.currentProject.id)
    }
  },
  methods: {
    ...mapActions([action.GET_POSTS]),
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
  }
}
</style>

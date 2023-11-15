<template>
  <section class="posts">
    <AccountAnalysisPostCard
      v-for="post in posts"
      :post-details="post"
      :key="post.id"
    />
  </section>
</template>

<script>
import AccountAnalysisPostCard from '@components/account-analysis/AccountAnalysisPostCard'

export default {
  name: 'AccountActivityPostsLayout',
  components: {
    AccountAnalysisPostCard,
  },
  props: {
    posts: {type: Array, required: true},
  },
}
</script>

<style lang="scss" scoped>
.posts {
  display: grid;
  grid-template-columns: 45% 2fr;

  gap: 50px;
  margin-bottom: 50px;
}
</style>

<template>
  <section class="posts">
    <MentionsPostCard
      v-for="post in posts"
      :post-details="post"
      :key="post.id"
    />
  </section>
</template>

<script>
import MentionsPostCard from '@/components/account-analysis/MentionsPostCard'

export default {
  name: 'MentionsPostsLayout',
  components: {MentionsPostCard},
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

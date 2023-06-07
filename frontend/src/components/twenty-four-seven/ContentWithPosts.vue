<template>
  <section class="view-content-wrapper scroll">
    <TFSPostCard
      :postDetails="post.online_post"
      :is-back="post.is_back"
      :card-status="post.status"
      :item-id="post.id"
      class="post-card"
    />

    <div class="related-content">
      <div class="title-wrapper">
        <span class="title">Related content</span>
        <span class="results">{{ relatedContent.length }} results</span>
      </div>

      <TFSPostCard
        v-for="(item, index) in relatedContent"
        :key="'related' + index"
        :postDetails="item.online_post"
        :is-back="item.is_back"
        :card-status="item.status"
        :item-id="item.id"
        :is-related-content="true"
        class="post-related-content"
      />
    </div>
  </section>
</template>

<script>
import TFSPostCard from '@/components/TFSPostCard'

export default {
  name: 'ContentWithPosts',
  components: {
    TFSPostCard,
  },
  props: {
    post: {type: Object, requied: true},
    relatedContent: {type: Array, requied: true},
  },
}
</script>

<style lang="scss" scoped>
.view-content-wrapper {
  flex: 1;
  height: 685px;
  padding: 24px 24px 0 0;
  margin: -24px -24px -24px 0;

  .post-card {
    width: 100%;
  }

  .related-content {
    display: flex;
    flex-direction: column;

    margin-top: 40px;

    .title-wrapper {
      display: flex;
      align-items: center;
      gap: 12px;

      margin-bottom: 28px;

      font-weight: 600;

      .title {
        font-size: 20px;
        color: var(--typography-primary-color);
      }

      .results {
        font-size: 14px;
        color: var(--typography-secondary-color);
      }
    }

    .post-related-content {
      width: 100%;
      margin-bottom: 20px;

      background: var(--primary-active-color);
    }
  }
}
</style>

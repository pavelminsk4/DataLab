<template>
  <section class="view-content-wrapper scroll">
    <TFSPostCard
      :postDetails="post.online_post"
      :is-back="post.is_back"
      :card-status="post.status"
      :item-id="post.id"
      :is-show-statuses-dropdown="false"
      class="post-card"
    />

    <div class="related-content">
      <div class="title-wrapper">
        <span class="title">Related content</span>
        <span class="results">{{ relatedContent.length }} results</span>
      </div>

      <BaseSpinner v-if="relatedContentLoading" />

      <TFSPostCard
        v-else
        v-for="(item, index) in relatedContent"
        :key="'related' + index"
        :postDetails="item.online_post"
        :is-back="item.is_back"
        :card-status="item.status"
        :item-id="item.id"
        :is-related-content="true"
        :is-work-button-show="true"
        :is-show-statuses-dropdown="false"
        :is-checkbox-show="isShowRelatedContent"
        :selected-post="linkedContentProxy"
        class="post-related-content"
        @open-modal="$emit('open-modal', item)"
        @add-related-content="addRelatedContent"
      />
    </div>
  </section>
</template>

<script>
import TFSPostCard from '@/components/TFSPostCard'
import BaseSpinner from '@/components/BaseSpinner'

const PUBLISHED = 'Published'

export default {
  name: 'ContentWithPosts',
  components: {
    TFSPostCard,
    BaseSpinner,
  },
  props: {
    post: {type: Object, requied: true},
    relatedContent: {type: Array, requied: true},
    relatedContentLoading: {type: Boolean, requied: true},
  },
  data() {
    return {
      linkedContent: null,
    }
  },
  computed: {
    currentLinkedPosts() {
      return this.post.linked_items.map((post) => post.id)
    },
    linkedContentProxy: {
      get() {
        return this.linkedContent || this.currentLinkedPosts
      },
      set(value) {
        this.linkedContent = value
      },
    },
    isShowRelatedContent() {
      return this.post.status !== PUBLISHED
    },
  },
  methods: {
    addRelatedContent(items) {
      this.linkedContentProxy = items
      this.$emit('add-related-content', this.linkedContent)
    },
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
    align-items: center;

    margin-top: 40px;

    .title-wrapper {
      display: flex;
      align-items: center;
      gap: 12px;

      width: 100%;
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

<template>
  <div class="post-title">
    {{ title }}
  </div>
  <div class="post-description">
    {{ description }}
  </div>
</template>

<script>
export default {
  name: 'TFSOriginalContentTab',
  emits: ['save-summary'],
  props: {
    post: {type: Object, required: true},
  },
  computed: {
    title() {
      return this.post.online_post.entry_title
    },
    description() {
      return this.post.online_post.entry_summary
    },
  },
}
</script>

<style lang="scss" scoped>
.post-title {
  margin: 0 0 16px;

  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 28px;
  color: var(--typography-title-color);
}

.post-description {
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-primary-color);
}
</style>

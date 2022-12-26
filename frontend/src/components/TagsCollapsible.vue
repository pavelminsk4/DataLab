<template>
  <div class="tags">
    <span v-for="tag in displayedTags" :key="tag" class="tag">
      {{ tag }}
    </span>
    <div
      v-if="isDisplayedCollapseBtn"
      class="tag tag-collapse"
      @click.stop="toggleCollapsed"
    >
      <PointsIcon v-if="isCollapsed" class="dots-icon" />
      <CrossIcon v-else />
    </div>
  </div>
</template>

<script>
import CrossIcon from '@components/icons/CrossIcon'
import PointsIcon from '@components/icons/PointsIcon'

const DISPLAYED_TAGS = 2

export default {
  name: 'TagsCollapsible',
  components: {CrossIcon, PointsIcon},
  props: {
    tags: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {isCollapsed: true}
  },
  computed: {
    isDisplayedCollapseBtn() {
      return this.tags.length > DISPLAYED_TAGS
    },
    displayedTags() {
      return this.isCollapsed && this.isDisplayedCollapseBtn
        ? this.tags.slice(0, DISPLAYED_TAGS)
        : this.tags
    },
  },
  methods: {
    toggleCollapsed() {
      this.isCollapsed = !this.isCollapsed
    },
  },
}
</script>

<style lang="scss" scoped>
.tags {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: -6px;
}

.tag {
  width: fit-content;
  height: 25px;
  padding: 2px 12px;
  margin-bottom: 6px;

  border-radius: 8px;
  background: rgba(51, 204, 112, 0.2);

  font-weight: 400;
  font-size: 14px;

  color: #30f47e;

  &:not(:last-child) {
    margin-right: 6px;
  }
}

.tag-collapse {
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.dots-icon {
  height: 15px;
}
</style>

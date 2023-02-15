<template>
  <div class="tags">
    <span v-for="tag in displayedTags" :key="tag" class="tag">
      {{ tag }}
    </span>
    <div v-if="isDisplayedCollapseBtn">
      <div v-if="isCollapsed" class="number-others-tags">
        +{{ numberOthersTags }}
      </div>
      <CrossIcon v-else />
    </div>
  </div>
</template>

<script>
import CrossIcon from '@components/icons/CrossIcon'

const DISPLAYED_TAGS = 2

export default {
  name: 'TagsCollapsible',
  components: {CrossIcon},
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
    numberOthersTags() {
      return this.isDisplayedCollapseBtn ? this.tags.length - DISPLAYED_TAGS : 0
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
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: -6px;
}

.tag {
  overflow: hidden;
  width: fit-content;
  height: 25px;
  padding: 2px 12px;
  margin-bottom: 6px;

  border-radius: 2px 12px 12px 2px;
  background: var(--neutral-secondary-color);

  font-weight: 400;
  font-size: 14px;

  color: var(--neutral-primary-color);

  &:not(:last-child) {
    margin-right: 6px;
  }
}

.tag-collapse {
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.number-others-tags {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;

  width: 30px;
  height: 30px;
  margin-bottom: 6px;

  font-weight: 500;
  font-size: 10px;
  color: var(--typography-title-color);
}
</style>

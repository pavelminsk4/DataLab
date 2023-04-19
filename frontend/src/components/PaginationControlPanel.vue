<template>
  <BaseDropdown
    name="posts-on-page"
    custom-style="top: auto; bottom: 25px"
    :selected-value="countPosts"
  >
    <div
      v-for="(item, index) in postsOnPage"
      :key="'drop' + index"
      @click="updatePostsCount(item)"
    >
      {{ item }}
    </div>
  </BaseDropdown>

  <VPagination
    v-model="page"
    :pages="pages"
    :range-size="1"
    active-color="#BB3D6E"
    container-class="pagination"
  />
</template>

<script>
import VPagination from '@hennge/vue3-pagination'
import '@hennge/vue3-pagination/dist/vue3-pagination.css'

import BaseDropdown from '@/components/BaseDropdown'

export default {
  name: 'PaginationControlPanel',
  components: {BaseDropdown, VPagination},
  emits: ['update-page', 'update:modelValue'],
  props: {
    pages: {type: Number, required: true},
    modelValue: {type: Number, default: 1},
    countPosts: {type: Number, default: 20},
    postsOnPage: {type: Array, required: true},
  },
  data() {
    return {
      newCurrentPage: null,
    }
  },
  computed: {
    page: {
      get() {
        return this.modelValue
      },
      set(value) {
        this.$emit('update:modelValue', value)
        this.$emit('update-page', value, this.countPosts)
      },
    },
  },
  methods: {
    updatePostsCount(value) {
      this.$emit('update:modelValue', 1)
      this.$emit('update-page', 1, value)
    },
  },
}
</script>

<style lang="scss">
.pagination {
  display: flex;
  gap: 4px;

  .PaginationControl {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 20px;
    height: 20px;

    background: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: 6px;

    color: var(--typography-title-color);

    .Control {
      fill: var(--typography-title-color);
    }

    .Control-active {
      fill: var(--typography-title-color);
    }
  }

  .Page-active {
    color: var(--button-text-color) !important;
  }

  .Page {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 32px;
    height: 22px;

    background: var(--primary-active-color);
    border: var(--border-primary);
    border-radius: 6px;

    color: var(--typography-primary-color);
  }
}
</style>

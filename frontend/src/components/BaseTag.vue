<template>
  <div class="base-tag">
    <div
      v-for="(tag, index) in tags"
      :key="index"
      :class="['input-tag', isMainField ? 'input-main' : 'input-key']"
    >
      <div class="tag-container">
        {{ tag }}
      </div>

      <DeleteTagButton
        @click="removeTag(index)"
        :class="[
          'delete-tag',
          isMainField ? 'delete-tag-main' : 'delete-tag-key',
        ]"
      />
    </div>
    <input
      type="text"
      :placeholder="placeholder"
      @keydown="addTag"
      @keydown.delete="removeLastTag"
      class="input-text"
    />
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import {action} from '@store/constants'

import DeleteTagButton from '@components/icons/DeleteTagButton'

export default {
  name: 'BaseTag',
  components: {DeleteTagButton},
  props: {
    placeholder: {
      type: String,
      default: 'Enter text',
    },
    isMainField: {
      type: Boolean,
      default: false,
    },
    value: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      tags: [],
    }
  },
  methods: {
    ...mapActions([action.UPDATE_KEYWORDS_LIST, action.CLEAR_KEYWORDS_LIST]),
    async updateKeywords(keywords) {
      await this[action.UPDATE_KEYWORDS_LIST](keywords)
    },
    async addTag(event) {
      if (event.code === 'Comma' || event.code === 'Enter') {
        event.preventDefault()
        let val = event.target.value.trim()

        if (val.length > 0) {
          this.tags.push(val)
          await this.updateKeywords([val])
          event.target.value = ''
        }
      }
    },
    async removeTag(index) {
      this.tags.splice(index, 1)
      await this[action.CLEAR_KEYWORDS_LIST](index)
    },
    async removeLastTag(event) {
      if (event.target.value.length === 0) {
        await this.removeTag(this.tags.length - 1)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.base-tag {
  display: flex;
  align-items: center;

  height: 44px;
  width: 100%;
  padding: 0 15px 0 10px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  overflow: auto;

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 10px;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}

.input-tag {
  display: flex;
  align-items: center;
  justify-content: center;

  margin-right: 10px;
  padding: 0 8px 0 10px;

  border-radius: 8px;
}

.tag-container {
  display: flex;
  justify-content: space-between;
  align-items: center;

  width: 100%;

  box-sizing: border-box;

  white-space: nowrap;

  &::-webkit-scrollbar {
    height: 3px;
  }

  &::-webkit-scrollbar-track {
    box-shadow: inset 0 0 5px grey;
    border-radius: 100px;
  }

  &::-webkit-scrollbar-thumb {
    background: var(--progress-line);
    border-radius: 10px;
  }
}

.input-main {
  background: rgba(51, 204, 112, 0.2);

  color: var(--tag-color);
}

.input-key {
  background: rgba(231, 167, 71, 0.2);

  color: var(--key-word-color);
}

.delete-tag {
  cursor: pointer;

  margin-left: 12px;
}

.delete-tag-key {
  color: var(--key-word-color);
}

.delete-tag-main {
  color: var(--tag-color);
}

.input-text {
  min-width: 100%;

  border: none;
  outline: none;
  background: none;

  color: var(--primary-text-color);
}
</style>

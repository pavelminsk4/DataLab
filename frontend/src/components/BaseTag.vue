<template>
  <div class="base-tag">
    <div
      v-for="(tag, index) in tags"
      :key="index"
      :class="['input-tag', isMainField ? 'input-main' : 'input-key']"
    >
      {{ tag }}
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
import DeleteTagButton from '@/components/icons/DeleteTagButton'
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
  },
  data() {
    return {
      tags: ['hello', 'hey'],
    }
  },
  methods: {
    addTag(event) {
      if (event.code === 'Comma' || event.code === 'Enter') {
        event.preventDefault()
        let val = event.target.value.trim()

        if (val.length > 0) {
          this.tags.push(val)
          event.target.value = ''
        }
      }
    },
    removeTag(index) {
      this.tags.splice(index, 1)
    },
    removeLastTag(event) {
      if (event.target.value.length === 0) {
        this.removeTag(this.tags.length - 1)
      }
    },
  },
}
</script>

<style scoped>
.base-tag {
  display: flex;
  align-items: center;

  height: 44px;
  width: 100%;
  padding-left: 10px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  overflow: auto;
}

.base-tag::-webkit-scrollbar {
  height: 5px;
  width: 5px;
}

.base-tag::-webkit-scrollbar-track {
  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  border-radius: 10px;
}

.base-tag::-webkit-scrollbar-thumb {
  height: 4px;

  background: var(--secondary-text-color);
  border-radius: 10px;
}

.input-tag {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 25px;
  margin-right: 10px;
  padding: 4px 8px 5px 10px;

  border-radius: 8px;
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
  width: 100%;

  border: none;
  outline: none;
  background: none;

  color: var(--primary-text-color);
}
</style>

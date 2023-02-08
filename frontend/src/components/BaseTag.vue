<template>
  <div :class="['tag-input scroll', hasError && 'error']">
    <div
      v-for="(tag, index) in tags"
      :key="tag"
      :class="[
        {
          duplicate: tag === duplicate,
          tag: tagsClass.length === 0,
        },
        'tag-value',
        isAdditionalKeywords && 'additional-keyword',
        isIrrelevantKeywords && 'irrelevant-keyword',
      ]"
    >
      {{ tag }}
      <DeleteTagButton class="delete" @click="removeTag(index)" />
    </div>

    <input
      v-model="newTag"
      type="text"
      :list="id"
      :name="name"
      autocomplete="off"
      @keydown.enter="addTag(newTag)"
      @keydown.prevent.tab="addTag(newTag)"
      @keydown.delete="newTag.length || removeTag(tags.length - 1)"
      @input="addTagIfDelem(newTag)"
      :placeholder="placeholder"
      class="input"
    />

    <div v-if="hasError" class="error-container">
      {{ errorMessage }}
      <ErrorIcon class="error-icon" />
    </div>
  </div>
</template>

<script>
import {ref, watch, nextTick, onMounted} from 'vue'
import DeleteTagButton from '@/components/icons/DeleteTagButton'
import ErrorIcon from '@/components/icons/ErrorIcon'

export default {
  name: 'BaseTag',
  components: {ErrorIcon, DeleteTagButton},
  props: {
    modelValue: {
      type: Array,
      default: () => [],
    },
    allowCustom: {
      type: Boolean,
      default: true,
    },
    tagClass: {
      type: String,
      default: '',
    },
    name: {
      type: String,
      default: '',
    },
    isAdditionalKeywords: {
      type: Boolean,
      default: false,
    },
    placeholder: {
      type: String,
      default: 'Enter text',
    },
    isIrrelevantKeywords: {
      type: Boolean,
      default: false,
    },
    textarea: {
      type: Boolean,
      default: false,
    },
    hasError: {
      type: Boolean,
      default: false,
    },
    errorMessage: {
      type: String,
      default: 'Error',
    },
    customDelimiter: {
      type: [String, Array],
      default: () => [],
      validator: (val) => {
        if (typeof val == 'string') return val.length == 1
        for (let i = 0; i < val.length; i++) {
          if (typeof val[i] != 'string' || val[i].length != 1) return false
        }
        return true
      },
    },
  },
  setup(props, {emit}) {
    const tags = ref(props.modelValue)
    const tagsClass = ref(props.tagClass)
    const newTag = ref('')
    const id = Math.random().toString(36).substring(7)
    const customDelimiter = [
      ...new Set(
        (typeof props.customDelimiter == 'string'
          ? [props.customDelimiter]
          : props.customDelimiter
        ).filter((it) => it.length == 1)
      ),
    ]
    const duplicate = ref(null)
    const handleDuplicate = (tag) => {
      duplicate.value = tag
      setTimeout(() => (duplicate.value = null), 1000)
      newTag.value = ''
    }

    const addTag = (tag) => {
      tag = tag.trim()
      if (!tag) return
      if (!props.allowCustom) return
      if (tags.value.includes(tag)) {
        handleDuplicate(tag)
        return
      }
      tags.value.push(tag)
      newTag.value = ''
      emit('start-search')
    }
    const addTagIfDelem = (tag) => {
      if (!customDelimiter || customDelimiter.length == 0) return
      if (customDelimiter.includes(tag.charAt(tag.length - 1)))
        addTag(tag.substr(0, tag.length - 1))
    }
    const removeTag = (index) => {
      tags.value.splice(index, 1)
    }

    const onTagsChange = () => {
      emit('update:modelValue', props.name, tags.value)
    }
    // eslint-disable-next-line vue/valid-next-tick
    watch(tags, () => nextTick(onTagsChange), {deep: true})
    onMounted(onTagsChange)

    return {
      tags,
      tagsClass,
      newTag,
      addTag,
      addTagIfDelem,
      removeTag,
      id,
      duplicate,
    }
  },
}
</script>

<style lang="scss" scoped>
.tag-input {
  position: relative;

  display: flex;
  flex-wrap: wrap;
  align-items: center;

  max-height: 110px;
  height: 40px;
  width: 100%;
  padding: 4px 8px;

  border: 1px solid var(--border-color);
  border-radius: 10px;
  background: var(--background-secondary-color);

  overflow: auto;

  .input {
    flex-grow: 1;

    min-width: 40px;

    border: none;
    outline: none;
    background: none;

    color: var(--primary-text-color);
  }

  .tag-value {
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    gap: 4px;

    padding: 2px 8px;

    border-radius: 2px 12px 12px 2px;

    color: var(--neutral-primary-color);
    background-color: var(--neutral-secondary-color);

    .delete {
      cursor: pointer;
    }
  }
}

.tag-input .additional-keyword {
  background: var(--positive-secondary-color);

  color: var(--positive-primary-color);
}

.tag-input .irrelevant-keyword {
  background: var(--negative-secondary-color);

  color: var(--negative-primary-color);
}

.tag-input .duplicate {
  color: var(--primary-text-color);

  background: var(--negative-status);
  animation: shake 1s;
}

.error {
  border: 1px solid var(--negative-status);
  border-radius: 10px;

  .error-container {
    position: absolute;
    right: 10px;

    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;

    white-space: nowrap;

    color: var(--negative-status);

    .error-icon {
      margin-right: 15px;
    }

    font-size: 12px;
  }
}

@keyframes shake {
  10%,
  90% {
    transform: scale(0.9) translate3d(-1px, 0, 0);
  }
  20%,
  80% {
    transform: scale(0.9) translate3d(2px, 0, 0);
  }
  30%,
  50%,
  70% {
    transform: scale(0.9) translate3d(-4px, 0, 0);
  }
  40%,
  60% {
    transform: scale(0.9) translate3d(4px, 0, 0);
  }
}
@keyframes shake1 {
  10%,
  90% {
    transform: scale(0.99) translate3d(-1px, 0, 0);
  }
  20%,
  80% {
    transform: scale(0.98) translate3d(2px, 0, 0);
  }
  30%,
  50%,
  70% {
    transform: scale(1) translate3d(-4px, 0, 0);
  }
  40%,
  60% {
    transform: scale(0.98) translate3d(4px, 0, 0);
  }
}
</style>

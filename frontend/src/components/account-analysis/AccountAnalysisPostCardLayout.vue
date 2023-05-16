<template>
  <div :class="['post-card', `${postDetails.sentiment}-border`]">
    <div class="post-card__body">
      <div v-if="checkType('reply')" class="post-card__reply">
        <RepliesIcon />
        <span
          >Replying to
          <span class="alias">@{{ postDetails.inreplyto }}</span>
        </span>
      </div>
      <div v-if="checkType('retweet')">Retweet</div>
      <div class="post-card__text">
        {{ postDetails.text }}
      </div>
      <div class="post-card__chips">
        <div class="chips__container">
          <BaseChips :chips-type="postDetails.sentiment" />
        </div>
        <div class="chips__container">
          <BaseChips chips-type="topic"> Topic</BaseChips>
        </div>
      </div>
    </div>
    <div class="post-card__footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script>
import {isAllEmptyFields} from '@lib/utilities'

import BaseChips from '@/components/BaseChips'
import RepliesIcon from '@/components/icons/RepliesIcon'

export default {
  name: 'PostCardLayout',
  components: {
    RepliesIcon,
    BaseChips,
  },
  props: {
    postDetails: {type: Object, required: true},
  },
  methods: {
    checkType(type) {
      if (!isAllEmptyFields(this.postDetails))
        return this.postDetails.type.includes(type)
    },
  },
}
</script>

<style lang="scss" scoped>
.post-card {
  height: 210px;

  background: var(--background-secondary-color);

  box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);
  border-radius: 8px;

  &__body {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    padding: 20px 20px 10px;

    height: 75%;
  }

  &__reply {
    display: flex;
    align-items: center;

    gap: 10px;
    .alias {
      color: var(--primary-color);
    }
  }

  &__text {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  &__chips {
    display: flex;

    gap: 8px;
    .chips__container {
      height: fit-content;
    }
  }

  &__footer {
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-around;

    padding: 10px 0px 5px 20px;

    height: 25%;

    border-top: var(--border-primary);
  }
}
.neutral-border {
  border-left: 3px solid var(--neutral-primary-color);
}

.positive-border {
  border-left: 3px solid var(--positive-primary-color);
}

.negative-border {
  border-left: 3px solid var(--negative-primary-color);
}
</style>

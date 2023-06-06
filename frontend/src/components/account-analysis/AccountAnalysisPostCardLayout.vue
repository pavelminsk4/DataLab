<template>
  <div :class="['post-card', `${postDetails.sentiment}-border`]">
    <div class="post-card__body">
      <slot></slot>
    </div>
    <div class="post-card__footer">
      <div class="option">
        <h4>Date</h4>
        <span class="option__text"> {{ formateDate(postDetails.date) }}</span>
      </div>
      <div class="option">
        <h4>Engagements</h4>
        <span class="option__text"> {{ postDetails.engagements }}</span>
      </div>
      <div class="option stat">
        <LikeIcon />
        <span> {{ postDetails.count_favorites }}</span>
      </div>
      <div class="option stat">
        <RepliesIcon />
        <span> {{ postDetails.count_replies }}</span>
      </div>
      <div class="option stat">
        <RetweetsIcon />
        <span> {{ postDetails.count_totalretweets }}</span>
      </div>
      <div class="option stat">
        <a :href="postDetails.link" target="_blank" class="link">&#8599;</a>
      </div>
    </div>
  </div>
</template>

<script>
import RepliesIcon from '@/components/icons/RepliesIcon'

import LikeIcon from '@/components/icons/LikeIcon'
import RetweetsIcon from '@/components/icons/RetweetsIcon'

export default {
  name: 'PostCardLayout',
  components: {
    RepliesIcon,
    LikeIcon,
    RetweetsIcon,
  },
  props: {
    postDetails: {type: Object, required: true},
  },
  methods: {
    formateDate(date) {
      return new Date(date)
        .toLocaleString()
        .split(', ')
        .reverse()
        .join(', ')
        .replaceAll('/', '.')
    },
  },
}
</script>

<style lang="scss" scoped>
.post-card {
  height: fit-content;

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

.option {
  display: flex;
  flex-direction: column;
  justify-content: center;

  width: 100%;

  padding-right: 5px;

  border-right: var(--border-primary);

  &:nth-child(n + 1) {
    padding-left: 5px;
  }

  &:last-child {
    border-right: none;
  }

  &__text {
    font-weight: 400;
    font-size: 11px;
  }

  .link {
    text-decoration: none;
    color: var(--primary-color);
    font-size: 25px;
  }
}

.stat {
  align-items: center;
  flex-direction: row;

  gap: 5px;
}
h4 {
  font-weight: 500;
  font-size: 10px;

  text-transform: uppercase;
  color: var(--typography-secondary-color);
}

span {
  font-size: 12px;
}
</style>

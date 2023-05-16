<template>
  <post-card-layout :post-details="postDetails">
    <template #footer>
      <div class="option">
        <h4>Date</h4>
        <span class="option__text"> {{ formateDate(postDetails.date) }}</span>
      </div>
      <div class="option">
        <h4>Engagements</h4>
        <span class="option__text"> {{ postDetails.engagement }}</span>
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
    </template>
  </post-card-layout>
</template>

<script>
import PostCardLayout from '@/components/account-analysis/PostCardLayout2'
import LikeIcon from '@/components/icons/LikeIcon'
import RepliesIcon from '@/components/icons/RepliesIcon'
import RetweetsIcon from '@/components/icons/RetweetsIcon'

export default {
  name: 'AccountAnalysisPostCard',
  components: {
    PostCardLayout,
    LikeIcon,
    RepliesIcon,
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

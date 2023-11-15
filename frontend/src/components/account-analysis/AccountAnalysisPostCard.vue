<template>
  <account-analysis-post-card-layout :post-details="postDetails">
    <div class="card-body">
      <div v-if="checkType('reply')" class="card-body__reply">
        <RepliesIcon />
        <span>
          Replying to
          <span class="alias">@{{ postDetails.inreplyto }}</span>
        </span>
      </div>
      <div v-if="checkType('retweet')">Retweet</div>
      <div class="card-body__text">
        {{ postDetails.text }}
      </div>
      <div class="card-body__chips">
        <div class="chips__card-body">
          <SentimentChips
            :chips-type="postDetails.sentiment"
            :post-id="postDetails.id"
          />
        </div>
        <div class="chips__card-body">
          <BaseChips chips-type="topic">
            <CustomText tag="span" text="Topic" />
          </BaseChips>
        </div>
      </div>
    </div>
  </account-analysis-post-card-layout>
</template>

<script>
import CustomText from '@components/CustomText'
import AccountAnalysisPostCardLayout from '@components/account-analysis/AccountAnalysisPostCardLayout'
import SentimentChips from '@components/SentimentChips'
import BaseChips from '@components/BaseChips'
import RepliesIcon from '@components/icons/RepliesIcon'

import {isAllFieldsEmpty} from '@lib/utilities'

export default {
  name: 'AccountAnalysisPostCard',
  components: {
    AccountAnalysisPostCardLayout,
    SentimentChips,
    BaseChips,
    RepliesIcon,
    CustomText,
  },
  props: {
    postDetails: {type: Object, required: true},
  },
  methods: {
    checkType(type) {
      if (!isAllFieldsEmpty(this.postDetails))
        return this.postDetails.type.includes(type)
    },
  },
}
</script>

<style lang="scss" scoped>
.card-body {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  gap: 20px;
  height: 100%;

  cursor: pointer;

  &__chips {
    display: flex;

    gap: 8px;
    .chips__container {
      height: fit-content;
    }
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
}
</style>
